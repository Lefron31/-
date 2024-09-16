# 집합(set)
# 중복 안됨, 순서 없음

set_1 = {1,2,3,3,3}
print(set_1)

java = {'유재석', '김태호', '양세형'}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합 ( java는 가능하지만 python을 모르는 사람 )
print(java - python)
print(java.difference(python))

# python이 가능한 사람이 늘어남
python.add('김태호')
print(python)

# 값 제거
java.remove('김태호')
print(java)