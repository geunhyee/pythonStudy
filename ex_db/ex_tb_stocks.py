import sqlite3
import requests
import json
import  datetime
url = "https://api.upbit.com/v1/market/all"
sql = """ INSERT INTO tb_stocks VALUES(:1, :2, :3)"""
res = requests.get(url)
text = res.text
json_data = json.loads(text)
conn = sqlite3.connect("mydb.db")
cur = conn.cursor()
for row in json_data:
    cur.execute(sql, [row['market'], row['korean_name'], row['english_name']])
# sql = """ CREATE TABLE tb_stocks(
#         stock_code VARCHAR2(20)
#         ,stock_kr VARCHAR2(100)
#         ,stock_en VARCHAR2(100)
#         )
#         """
# sql = "SELECT*FROM tb_stocks"
conn.commit()

cur.execute("SELECT * FROM tb_stocks")
rows = cur.fetchall()
print(rows)
conn.close()
url = "https://api.upbit.com/v1/ticker?markets="
for row in rows:
    print(url+ row[0])
    res = requests.get(url + row[0])
    if res.status_code ==200:
        json_data = json.loads(res.text)
        market = json_data[0]['market']
        trade_price = "{:.15F}".format(json_data[0]['trade_price'])
        trade_timestamp = json_data[0]['timestamp'] * 0.001 #초단위로 변환
        str_timestamp = datetime.datetime.fromtimestamp(trade_timestamp).strftime("%Y-%m-%d %H:%M:%S")
        sql = """ INSERT INTO tb_stocks VALUES(:1, :2, :3)
        """
        # print(market,trade_price,str_timestamp)

conn.commit()