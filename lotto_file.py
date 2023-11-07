import  random
# def fn_lotto(user_num):
#     arr = []
#     for i in range(user_num):
#         lotto = set()
#         while True :
#             lotto.add(random.randint(1,45)) #랜덤 정수 1~45
#             if len(lotto) == 6:
#                 break
#         arr.append(lotto)
#     print("good luck")
#     return  arr


# 사용자가 로또 번호에 포함시키고 싶은 번호를 입력받아
# 원하는 수량 만큼 로또 번호를 생성해 주세요
# param1 = 수량, param2: 0~6개의 1~45 사이 수
user_input= input("로또 수량과 희망하는 숫자를 띄어쓰기로 입력해주세요")
user_split = user_input.split()
user_num = int(user_split[0])

def fn_lotto2():
    arr=[]
    while len(user_input) == 0:
        lotto = set()
        lotto.add(random.randint(1,45))
        if len(lotto) ==6:
            break



# print(user)

# def fn_lotto2(user_num):
#     arr = []
#     for i in range(len(user_num)):
#         lotto = set()
#         while len(user_num) == 0 :
#             lotto.add(random.randint(1,45))
#             if len(lotto) ==6:
#                 break
#         return arr



# 1. 수량만 있을 경우
# 2.희망하는 숫자가 1~6일 경우
# 3.희망하는 숫자가 6개를 넘는 경우 -> 다시 입력 받기



#
# if __name__ == '__main__':      # 해당 모듈에서 자체 실행(test용)
#
#     my_lotto = fn_lotto(5)
#     print(my_lotto)
# else:
#     print("import 했을때")
