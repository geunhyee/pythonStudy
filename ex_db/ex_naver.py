import  requests
import DBManager as mydb
import  json
import naver_logger
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

db = mydb.DBManager()

insert_sql = """
    INSERT INTO stocks (item_code, stock_nm, close_price, compare_close)
    VALUES (:1, :2, :3, :4)
"""
def insertnaver():

    for i in range(1, 43):
    # for i in range(1, 2):
        url = "https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={0}&pageSize=50".format(str(i))
        print(url)
        res = requests.get(url)
        jsonObj = json.loads(res.text)
        stock_arr = jsonObj['stocks']
        print(stock_arr)
        #종목명, 종목코드, 종가, 변동가 출력

        for row in stock_arr:
            db.insert(insert_sql, [row['itemCode'],row['stockName'], row['closePrice'],row['compareToPreviousClosePrice']])

#logger & apscheduler & dbmanger 를 사용하여
#10분 단위로 저장 및 기록 남기기

log = naver_logger.make_logger()
log.debug('DEBUG message')
log.info('INFO message')
log.warning('WARNING message')

#apscheduler

sched.add_job(insertnaver, 'cron', minute='10')
sched.start()
