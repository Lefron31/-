try:
    print('나누기 전용 계산기입니다')
    nums = []
    nums.append(int(input('첫 번쨰 숫자를 입력하세요')))
    nums.append(int(input('두 번쨰 숫자를 입력하세요')))
    nums.append(int(nums[0]/nums[1]))
    print(f'{nums[0]} / {nums[1]} = {nums[2]}')
except ValueError: # 자료형 오류
    print('에러!')
except ZeroDivisionError as err: # 0으로 나눴을 떄
    print('0으로 나눌 수 없습니다')
except Exception as err: # 나머지 모든 오류
    print('알 수 없는오류')
    print(err)

# 사용자 지정 에러
class BigNumberError(Exception):
    pass

try:
    print('한 자리 숫자 나누기 전용 계산기')
    n1 = int(input('첫 숫자 입력 : '))
    n2 = int(input('둘쨰 숫자 입력 : '))
    if n1 or n2 >= 10:
        raise BigNumberError # 의도적인 에러처리
    
    print(f'{n1} / {n2} = {n1/n2}')
except ValueError:
    print('오류')
except BigNumberError:
    print('오류')
finally: # 반드시 실행되는 구문 (오류 상관 x)
    print('이용해주어 감사합니다')


