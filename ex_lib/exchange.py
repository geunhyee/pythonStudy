#pip install matplotlib
#pip install finance-datareader

import pandas as pd

import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm    #폰트
import os
import  sqlite3
from ex_db.DBManager import DBManager
db = DBManager()

import  datetime
end_date= datetime.date.today()
start_date= end_date - datetime.timedelta(days=30)

path = os.getcwd()
font_path = "H2GTRM.TTF"
font_nm = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_nm
plt.rcParams['axes.unicode_minus'] = False

exchange_usd = fdr.DataReader('USD/KRW', start_date, end_date)
exchange_jpy = fdr.DataReader('JPY/KRW', start_date, end_date)
exchange_eur = fdr.DataReader('EUR/KRW', start_date, end_date)
exchange_cny = fdr.DataReader('CNY/KRW')

exchange_codes=['USD/KRW', 'JPY/KRW', 'EUR/KRW', 'CNY/KRW']
exchange_names = ['달러(USD)', '엔화(JPY)', '유로(EUR)','위안화(CNY)']
plt.figure(figsize=(12, 6))
for i, code in enumerate(exchange_codes) :
    if code == 'CNY/KRW' :
        plt.plot(exchange_cny.index, exchange_cny['Close'], label = exchange_names[i])
    else:
        df = fdr.DataReader(code, start_date, end_date)
        plt.plot(df['Close'], label=exchange_names[i])

for code, name, data in [('USD/KRW', '달러(USD)', exchange_usd),
                         ('JPY/KRW','엔화(JPY)', exchange_jpy),
                         ('EUR/KRW', '유로(EUR)', exchange_eur),
                         ('CNY/KRW', '위안화(CNY)', exchange_cny)
                         ]:
    for index, row in data.iterrows():
        exchange_date = index.strftime('%Y-%m-%d')
        exchange_price = row['Close']
        insert_sql = f"INSERT INTO exchange (exchange_code, exchage_name, exchange_price, exchange_date) VALUES (:1, :2, :3, :4) "
        db.insert(insert_sql, [code, name, exchange_price, exchange_date])



plt.title('환율비교 그래프')        #제목
plt.xlabel('날짜')              #X축 라벨
plt.ylabel('환율')             #Y축 라벨
plt.legend()                    #범례표시
plt.grid(True)                  #그리드 표시 false안그려짐
plt.tight_layout()              #레이아웃조정
plt.show()                      #출력

#
# sql = """CREATE TABLE exchange (
#             exchange_code VARCHAR2(100)
#             ,exchage_name VARCHAR2(100)
#             ,exchange_price VARCHAR2(1000)
#             ,exchange_date date default SYSDATE
#             )
# """
# conn.execute(sql)

# conn.commit()
# conn.close()
