from random import *

print(random()) # 0.0 ~ 1.0미만의 임의의 값
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값

print(int(random() * 10 + 1)) # 1 ~ 10 이하

print(randrange(1, 45)) # 1 ~ 45 미만의 값

print(randint(1,45)) # 1 ~ 45 이하의 값