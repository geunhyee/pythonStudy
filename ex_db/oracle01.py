#pip install cx_Oracle  -> 터미널에 이 라이브러리 설치
import cx_Oracle
conn = cx_Oracle.connect("java", "oracle", "localhost:1521/xe")         #커넥션 맺는법
print(conn.version)
sql='''
    SELECT *
    FROM member
    WHERE mem_name LIKE '%' || :word || '%'
    ORDER BY mem_name ASC
'''
nm = input("검색하고 싶은 고객명 입력:")
d = { "word": nm}
with conn:                  #with를 쓰면 close를 안해도됨
    cur = conn.cursor()
    rows = cur.execute(sql, d)
    for row in rows:
        print(row)

