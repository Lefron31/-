python = 'Python is Amazinga'

print(python.lower())
print(python.upper())

print(python[0].isupper) # 변수의[숫자] 자리가 대문자인가

print(len(python)) # 변수의 자리수

print(python.replace('Python', 'Java')) # 앞 글자를 뒤 글자로 바꿈


index = python.index('n') # 없을 경우 오류
print(index)

index = python.index('a', index + 4) # a위치에서 두번쨰 글자부터 찾음 
print(index)

print(python.find("a")) # 없을 경우 -1 반환

print(python.count('n')) # n이 몇번 등장하는가