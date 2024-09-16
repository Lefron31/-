# 지하철 칸별로 10명, 20명, 30명

subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]

#조세호가 몇번째 칸에 타고 있는가?
print(subway.index("조세호")+1)

# 하하가 다음 정류장에서 탐
subway.append("하하")

# 정형돈이 유재석/조세호 사이에 탐 [유재석 정형돈 조세호 박명수 하하]
subway.insert(1, "정형돈")
print(subway)

# 뒤에서 한명씩 꺼냄
print(subway.pop())
print(subway)

# 같은 객체가 몇개 있는지 확인하기
subway.append('유재석')
print(subway)
print(subway.count('유재석'))

# 리스트 내 정렬
num = [5,2,4,3,1]
num.sort()
print(num)

# 순서 뒤집기 가능
num.reverse()
print(num)

# 모두 지우기
num.clear()
print(num)

# 다양한 자료형 사용
mix_list = ['조세호', 5, True]
print(mix_list)

# 리스트 확장
num = [5,2,4,3,1]
num.extend(mix_list)
print(num)

print(num[1])

# 섞기
from random import *
list3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(list3)

# 리스트 내의 내역 랜덤 추첨
selected = sample(list3, 4) # list3 내에서 랜덤으로 4개를 뽑음
print(selected)