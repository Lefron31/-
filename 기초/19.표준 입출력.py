print('Python', 'Java', sep=',',end='?') # ","가 들어가는 부분을 치환

print('무엇이 더 재밌을까요?')


import sys
print('Python', 'Java', file=sys.stdout)
print('Python', 'Java', file=sys.stderr)



scores = {'수학':0, '영어':50, '코딩':100}
for subject, score in scores.items():
    #print(subject,score)
    print(subject.ljust(3),str(score).rjust(4),sep=':')
    #ljust : 좌측정렬, rjust : 우측정렬

# 은행 대기순번표
for num in range(1,101):
    print(f'대기번호 : {str(num).zfill(3)}')

# zfill : 괄호만큼의 공간 확보 후 빈공간 0으로 채움

## 표준 입출력

answer = list(input('입력하시오 : ').split())
print(answer)