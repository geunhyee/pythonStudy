import cx_Oracle

class DBManager:
    def __init__(self):
        self.conn = None
        self.get_connection()
    def get_connection(self):
        try:
            self.conn = cx_Oracle.connect("exchange", "1234", "localhost:1521/xe")
            return self.conn
        except Exception as e:
            print("오류발생 :", str(e))
            return None

    def __del__(self):
        try:
            print("소멸자")
            if self.conn:
                self.conn.close()
        except Exception as err:
            print("__del__", str(err))

    def insert(self, query, param):

        cursor = self.conn.cursor()
        cursor.execute(query, param)
        self.conn.commit()
        cursor.close()

if __name__ == '__main__':
    maneger = DBManager()
    conn = maneger.get_connection()

    if conn:
        # 테이블 이름, 컬럼 이름, 값에 맞게 수정하세요
        table_name = 'exchange'
        column_names = ['exchange_code', 'exchage_name', 'exchange_price', 'exchange_date']
        values = ['test', 'test', 'test', 'test']

        maneger.insert(table_name, column_names, values)
        print("데이터 삽입 완료")

        # 연결 버전 확인
        print(conn.version)
    else:
        print("데이터베이스 연결 실패")







    # sql = """INSERT INTO exchange (exchange_code, exchage_name, exchange_price, exchange_date)
    #         VALUES (:1,:2,:3,:4)
    #     """

    #
    #
    # maneger.insert(sql, ['test','test','test'])
    # print(conn.version)