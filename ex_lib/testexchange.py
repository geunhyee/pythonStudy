import FinanceDataReader as fdr

import FinanceDataReader as fdr

# 홍콩 달러 환율 데이터 가져오기
exchange_hkd = fdr.DataReader('HKD/KRW')

print(exchange_hkd.head())