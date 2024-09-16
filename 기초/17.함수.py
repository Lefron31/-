def open_account():
    print('새로운 계좌가 개설되었습니다')

def deposit(balance, money):
    print(f'입금이 완료되었습니다. 잔액은 {balance+money}원 입니다')
    return balance + money

def withdraw(balance, money):
    print(f'{money}원 출금하셨습니다. 잔액은 {balance-money}원 입니다')
    return balance-money

balance = deposit(10, 2)
print(balance)

balance = withdraw(balance, 4)
print(balance)




def profile(name,age=17,language="c언어"): # 기본값 설정 (변수를 받지 않았을 떄 나오는값)
    print(f'이름 : {name}, 나이 : {age}, 언어 : {language}')

profile("유재석", 20, "자바")
profile('김태호', 19, "파이썬") 
profile('김종국')

# 가변인자

# def profile2(name,age,l1,l2,l3,l4,l5):
#     print(f'이름 : {name}, 나이 : {age},',end=" ")
#     print(l1,l2,l3,l4,l5)

# profile2('유재석','20','a','b','c','d','e')
# profile2('김태호','20','a','b','','','')

def profile2(name,age,*l):#(값이 추가될 때에는 *로 표현해주면 됨)
    print(f'이름 : {name}, 나이 : {age},',end=" ")
    for i in l:
        print(i, end=" ")
    print()

profile2('유재석','20','a','b','c','d','e')
profile2('김태호','20','a','b')

