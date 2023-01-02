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

