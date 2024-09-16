# 사전
cabinet = {3:"유재석", 100:'김태호'}
print(cabinet[3], cabinet[100])

print(cabinet.get(3))

# 없는 자료는 오류발생
# print(cabinet[5])

# get사용시 None 출력
print(cabinet.get(5))
print(cabinet.get(5, "Available"))

print(3 in cabinet) # True
print(5 in cabinet) # False


# 추가
cabinet[1] = "조세호"
print(cabinet)

cabinet[1] = "김종국"
print(cabinet)

#제거
del cabinet[1]
print(cabinet)

# key 출력
print(cabinet.keys())
# value 출력
print(cabinet.values())
# 같이 출력
print(cabinet.items())

#완전제거
cabinet.clear()
print(cabinet)
