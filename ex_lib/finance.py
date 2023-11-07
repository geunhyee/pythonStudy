#pip install matplotlib
#pip install finance-datareader
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm    #폰트
import os

import pandas as pd

path = os.getcwd()
font_path = "H2GTRM.TTF"
font_nm = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_nm
plt.rcParams['axes.unicode_minus'] = False

#국내/해외 지수, 환율정보, 국채금리정보
# apple = fdr.DataReader('AAPL')
# print(apple.head())
# apple['Close'].plot()
# plt.show()
#한국거래소 상장종목
# df_krx = fdr.StockListing('KRX')
# print(df_krx.head())
# KOSPI= df_krx[df_krx['Market'].str.contains('KOSPI')] #마켓이라는 컬럼에 코스피만 담은것
# print(KOSPI.columns)
# print(KOSPI.head(50))   #50개 출력
# #특정 날짜것만 조회할때 삼성, 2022년것
# df_samsung_2022 = fdr.DataReader('005930', '2022')
# #2000년부터 2022년까지 조회할때
# df_samsung_2000_2022 = fdr.DataReader('005930', '2000-01-01','2022-12-31')
#
# print(df_samsung_2000_2022.info()) #기본정보
# print(df_samsung_2000_2022.describe()) #기초통계량
#
#
# df_samsung_2000_2022['Close'].plot() #특정 컬럼만 시각화하기 위해서 close 사용
# plt.show()

#여러개 항목을 시각화
import  datetime
#오늘 날짜를 기준으로 1달 전의 날짜 계산
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=30)
print(start_date)
# 5개 종목 리스트(삼성, sk하이닉스, 셀트리온, 삼성바이오로직스, lg화학)
stocks = ['005930','000660','068270', '207940', '051910']
#종목 이름으로 나오게 하려면
nm = ['삼성', 'sk하이닉스', '셀트리온', '삼성바이오로직스', 'lg화학']
plt.figure(figsize=(12, 6))
#각 종목별로 주가 데이터 가져와서 그리기
for i, stock in enumerate(stocks) :
    df = fdr.DataReader(stock, start_date, end_date)
    plt.plot(df['Close'], label=nm[i])
    file_nm = '{0}_{1}_{2}.xlsx'.format(nm[i], start_date, end_date)        #엑셀로 저장하기
    writer = pd.ExcelWriter(file_nm, engine='xlsxwriter')
    df.to_excel(writer, 'sheet1')
    writer._save()

plt.title('stock price')        #제목
plt.xlabel('Date')              #X축 라벨
plt.ylabel('Price')             #Y축 라벨
plt.legend()                    #범례표시
plt.grid(True)                  #그리드 표시 false안그려짐
plt.tight_layout()              #레이아웃조정
plt.savefig("30일.png")          #파일로 저장
plt.show()                      #출력
