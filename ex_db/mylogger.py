import  logging
#로그 파일 생성
# 소프트웨어나 시스템이 실행중에 발생하는 이벤트를 시간 순서대로 기록한 파일
#버그 추적, 시스템 문제 해결, 사용자 활동 모니터링 및 다양한 용도로 사용
#날짜시간, 로그레벨(warnning, error, info, debug..)
#메세지 및 주요 원인
#ip 주소, 사용자 id,실행 시간...

def make_logger(name=None):
    #로그생성
    logger = logging.getLogger(name)
    #logger level
    logger.setLevel(logging.DEBUG)
    #formatter 설정
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    #handler 설정
    console = logging.StreamHandler()
    file_handler = logging.FileHandler(filename="logfile.log")
    console.setFormatter(logging.INFO)
    file_handler.setLevel(logging.DEBUG)
    #출력 format 지정
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    #logger에 handler 추가
    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger