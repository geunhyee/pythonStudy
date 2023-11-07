import sqlite3
conn = sqlite3.connect("mydb.db")
cur = conn.cursor()
#1. insert 문자열로
# cur.execute(""" INSERT INTO stocks VALUES(3, '비트', 'BT')""")
#2. dict
# dic = {'seq':4, 'stock_kr':'도지코인','stock_en':'DOGE'}
# cur.execute(""" INSERT INTO stocks VALUES(:seq, :stock_kr, :stock_en)""", dic)
#3. array or tuple
cur.execute(""" INSERT INTO stocks VALUES(?, ?, ?)""", [5, '이더리움', 'ETHER'])

conn.commit()
conn.close()