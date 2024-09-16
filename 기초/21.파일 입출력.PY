score_file = open('score.txt', 'w', encoding='utf8')
# open(파일 이름, 목적 (w = 덮어쓰기), utf8인코딩)

print('수학 : 0', file=score_file)
print('영어 : 50', file=score_file)
score_file.close()

# 'a' : append = 추가
score_file = open('score.txt', 'a', encoding='utf8')
score_file.write('과학 : 80')
score_file.write('\n코딩 : 100')
score_file.close()

# 'r' : 읽기(불러오기)
score_file = open('score.txt', 'r', encoding='utf8')
print(score_file.read())
score_file.close()

score_file = open('score.txt', 'r', encoding='utf8')
print(score_file.readline(),end = "")
print(score_file.readline(),end = "")
print(score_file.readline(),end = "")
print(score_file.readline())
score_file.close()
# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동

score_file = open('score.txt', 'r', encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()

#리스트로 저장
score_file = open('score.txt', 'r', encoding='utf8')
lines = score_file.readlines() # readlines : 리스트로 저장
for line in lines:
    print(line, end="")
score_file.close()







