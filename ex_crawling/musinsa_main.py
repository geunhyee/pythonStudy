from musinsa import fn_get_musinsa
all_arr =[]
for i in range(1, 101):
    try:
        print(i, ':page 수집')
        all_arr += fn_get_musinsa(i)
    except Exception as e:
        print(str(e))
print(all_arr)
import csv
with open('musinsa.csv', 'w', encoding='utf-8') as f:
    write = csv.writer(f, delimiter= '|', quotechar='"')
    write.writerows(all_arr)