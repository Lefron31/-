customer = "토르"
index = 5

while index >= 1:
    print(f"{customer}, 커피가 준비되었습니다 {index}번 남았어요")
    index -= 1
    if index == 0:
        print('커피가 폐기되었습니다')

customer1 = "아이언맨"
index = 1
while True:
    print(f"{customer}, 커피가 준비되었습니다 {index}회")
    index += 1
    if index == 10:
        break

#continue : 아래의 문장 실행하지 않고 처음부터 반복
absent = [2, 5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print(f'오늘 수업 여기까지. {student}는 교무실로 와')
        break
    print(f'{student}, 책을 읽어봐')


