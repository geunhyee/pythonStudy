'''
#반복문 for
arr = ["팽수", "길동","동길"]
print("-"*20)
#  방법1 : value만 필요할때
for v in arr:           # v는 식별자
    print(v)
# 방법2 단순 반복
for i in range(3):
    print("-"*20)
    print(i)
    print(arr[i])
    # 방법3: index, value가 필요할때
for i, v in enumerate(arr):
    print('인덱스:', i,'값:', v)
#인덱스만 필요할때
for i in range(len(arr)):
    print(i)

# 반복문 while
user_cnt = int(input("몇회?"))
cnt= 0
while cnt < user_cnt:
    cnt +=1
    if cnt == 2:
        continue # 입력받은 값이 2 일때 건너뛴다
    if cnt ==5:
        break
    print('hi', cnt)


# 함수
# 기본형태
# print(fn_name('nick')) 클래스가 아닌데 함수를 위에 쓰면 오류남
def fn_name(param):
    print('함수 내용')
    return param * 10
print(fn_name('팽수'))

# return 0~n 여러개 가능
def fn_name2(param):
    a = param.split()
    return a[0], a[1]
first, second = fn_name2('홍 길동')
print('first:', first, 'second', second)
nm = fn_name2('김 팽수')
print(nm)

# 예외처리 try .. except
def fn_add(param):
    try:
        msg = param[0] + param[1]
    except IndexError as arr:
        print("인덱스 에러")
        print(str(arr))
    except Exception as err:
        print(str(err))
    else:
        print("정상처리")
    finally:
        print('종료')
    print('함수 끝부분')
fn_add(['1','2'])


def fn_add2(param):
        msg = param[0] + param[1]
        print('함수 끝부분')
fn_add2(['hi'])
'''

# 함수 default 설정
def add3(i, j, x=1):
    return i + j + x
print(add3(2,3,))   # x는 디폴트 값이 설정 되어 있어서 매개변수가 입력되지 않으면 디폴드값으로 됨
print(add3(2,3,10))

print(add3(x=2, i=1, j=2)) #(매개변수)순서를 모르겠다 싶을때 쓸수있는 방법

#가변 길이 파라미터
#함수의 입력 파라미터의 수를 미리 알수없을때 0~ n개 설정 가능
#파라미터 앞에 * 붙임
def fn_total(*nums):
    tot = 0
    for n in nums:
        tot += n
    return tot
print(fn_total(1,2,3,4,5,6))
print(fn_total())
print(fn_total(10,100))
def fn_sum_nul(flag, *nums):
    if flag == '+':
        result = 0
        for v in nums:
            result += v
    elif flag == '*':
        result = 1
        for v in nums:
            result *= v
    return result
print(fn_sum_nul('+', 1,2,3,4))
print(fn_sum_nul('*',1,2,3,4))

# dict key - value 쌍을 요소로 가지는 자료형
# {} 사용
classmate = {'팽수:':100, '길동:':90, '동길:': 80 }
print(type(classmate), classmate)
print(classmate['팽수'])  # key로 value에 접근
classmate['팽수'] = 60    #수정
print(classmate['팽수'])
for key in classmate:
    print(key, classmate[key])
dic = {'팽수': None}
dic['팽수'] = [1,2,3,4]
print(dic['팽수'])
# python 3.6부터 순서 정보가 생김
for i, k in enumerate(classmate):
    print(i, k, classmate[k])