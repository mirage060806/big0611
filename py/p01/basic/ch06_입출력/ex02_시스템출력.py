# 시스템 출력
print("사과", "복숭아", "망고")
# 기본값: sep=" "
# 기본값 있는 sep와 end는 마지막 인자로 기록.
# 구문자: ,
print("사과", "복숭아", "망고", sep=",")

# 줄바꿈
# 기본값: end='\n'
print('이것은 문장.', end='\n')
print('문장.', end='\n')

# 줄바꿈x
print('이것은 문장.', end='')
print('문장.', end='')

# 문자열 연결: +
# 나이: 20살
age = 20
print('나이:' + str(age) + '살')

# 개행문자: \n
print("산토끼 토끼야\n어디를 가느냐\n깡총깡총 뛰어서\n어디를 가느냐")

# 문자열 포맷팅: 문자열.format()
'''
print('문자열.format(time))
print('메시지: {} {}'.format(값1, 값2, ...))
print('메시지: {0} {1}'.format(값1, 값2, ...))
'''
# 기본 포맷스트링
food = '치킨'
text = '나는 {}을 먹고싶다'
print(text.format(food))
print('나는 {}을 먹고싶다'.format('치킨'))

# 다중 값 치환
food1 = '피자'
food2 = '치킨'
text = '나는 {}, {}을 먹고싶다'
print(text.format(food1, food2))

text = '나는 {0}, {1}을 먹고싶다'
print(text.format(food1, food2))

text = '나는 {1}, {0}을 먹고싶다'
print(text.format(food1, food2))

# text = '나는 {food1}, {food2}을 먹고싶다'
# print(text.format(food1, food2))

print('나는 {0} {1}을 먹고 싶다. 우리집엔 {1}이 배달되지 않아 슬프다.'.format(food1, food2))
# IndexError

# 인덱스대신 변수이름으로
text = '{name}님, 반갑습니다. 요금은 {money}만원 입니다.'
print(text.format(name = '홍', money = 500))

# 문자열에 %s를 작성하여, 치환할 문자를 지정
food = '치킨'
print('나는 %s을 먹고 싶다.' %food)

# 숫자 포맷팅
# 소수점 둘째자리까지 표시
print('{:.2F}% 확신합니다.'.format(95.1234567))
print('{:.2F}% 확신합니다.'.format(95.12567))

# 천 단위마다 ,
print('한 달 휴대폰 요금은 {:,}원 입니다,'.format(10000000))