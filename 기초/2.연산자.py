print(1+1)
print(3-2)
print(5/2)
print(5*2)

print(2**3) # 2^3 = 8 (거듭제곱)
print(8%3) # 2 (나머지 구하기) 
print(8//3) # 2 (몫 구하기)

print(3 == 3) # 둘이 같다

print(1 != 3) # 같지 않다

print((3>0) and (3<5)) # and는 & 로 대체가능
print((3>0) or (3<5)) # or는 | 로 대체가능

num = 10
print(f'{num} 더하기 2는 {num + 2}입니다.')

num += 2 # num + 2
print(num)
num -= 2 # num - 2
print(num)


print(abs(-3)) # 절댓값 absolute 3
print(pow(4,2)) # 4^2 = 16
print(max(5, 12)) # 최댓값 반환 12
print(min(3,12)) # 최솟값 반환 3
print(round(3.12)) # 반올림 3

from math import * 

print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

