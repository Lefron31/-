for number in range(0,5):
    print(f'숫자 : {number}')


starbucks = ['아이언맨','토르','그루트']
for customer in starbucks:
    print(f'{customer}, 커피가 준비되었습니다')


# 한 줄로 끝나는 for문
# 출석번호가 1, 2, 3, 4, 앞에 100을 붙이기로 함 
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 전환
students = ['Iron Man', 'Thor', 'I am Groot']
students1 = [len(i) for i in students]
print(students1)

# 학생 이름을 대문자로 변환
students_upper = [str(i.upper()) for i in students]
print(students_upper)