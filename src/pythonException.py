### Section10 : Python Exception

### SyntaxError : 문법 에러
# print('Test)

# if True
#    pass

## NameError : 참조 변수 없음
# a = 10
# b = 15

# print(c)

## ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

## IndexError : 인덱스 범위 오버
# x = [10, 20, 30]
# print(x[0])
# print(x[3])

## Key Error
# dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}
# print(dic['hobby'])
# dictionary에서 호출할때는 get을 사용해야 오류가 안남(없을때 none)
# print(dic.get('hobby'))

## AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 시에 예외
# import time
# print(time.time())
# print(time.month())

## ValueError : 참조값이 없을때 발생
# x = [1, 5, 9]
# x.remove(10)
# x.index(10)

## FileNotFoundError
# f = open('test.txt', 'r')

## TypeError
# x = [1, 2]
# y = (1. 2)
# z = 'test'

# print(x + y)
# print(x + z)

## 예외처리 기본
## try : 에러가 발생할 가능성이 있는 코드 실햏
## except : 에러명1
## except : 에러명2
## else : 에러가 발생하지 않았을 경우 실행
## finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occured ValueError!')
except IndeError:
    print('Not found it! - IndexError Error')
except Exception:
    print('Error')
else:
    print('OK! else!')
finally:
    print('Default ')

# 예외처리는 하지 않지만 무조건 수행
try:
    print('try')
finally:
    print('ok finally')


## raise 키워드로 예외 직접 발생
try:
    a = 'Kim'
    if a == 'Kim':
        print('OK 허가!')
    else:
        raise ValueError
except ValueError:
    print('Problem')
except Exception as f:
    print(f)
else:
    print('OK')
