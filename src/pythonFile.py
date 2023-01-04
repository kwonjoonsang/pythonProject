# File Read
# 한글을 읽기 위해서는 File Open 시 encoding을 utf-8로 변환해줘야함
f = open('../resource/review.txt', 'r', encoding='utf-8')

content = f.read()
print(content)

f.close()

with open('../resource/review.txt', 'r', encoding='utf-8') as f:
    c = f.read()
    print(c)


with open('../resource/review.txt', 'r', encoding='utf-8') as f:
    for c in f:
        print(c)

with open('../resource/review.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(">", content)
    ## 파일 내용 포커싱이 끝으로 가버림
    content = f.read()
    print(">", content)

with open('../resource/review.txt', 'r', encoding='utf-8') as f:
    ## 1 라인을 읽는다
    line = f.readline()
    ## print(line)
    while line:
        print(line, end=' ')
        line = f.readline()

with open('../resource/review.txt', 'r', encoding='utf-8') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=' ***** ')

with open('../resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

with open('../resource/text.txt', 'a') as f:
    f.write('Goodman!!\n')

from random import randint

with open('../resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')

with open('../resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)

with open('../resource/text4.txt', 'w') as f:
    print('Test Contests1!', file=f)
    print('Test Contests2!', file=f)