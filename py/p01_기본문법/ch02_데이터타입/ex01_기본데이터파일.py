# 자료형
# 1. 숫자형
# 정수
x, y = 10, -25
# 실수
z = 3.14

# type(): 자료형 확인 내장 함수
print(type(x), type(y), type(z))

# 지수 펴현식(e: exponential)
# e(n) = 10의 상승 - 10*10*...
a = 17e3
b = 17E3
c = -35.2e2
d = 275e-2
print(a, b, c, d)

# 2. 불리언(bool): True, False - 논리값
# 대입 연산자: =
# 비교 연상자: > < ==
a = 100 > 50
b = 100 < 50
c = 100 == 50
print(a, b, c)
type(a)

# 3. 문자형(str): "", ''
a = "Hello"
b = '123' 
c = 'How are you?'
# 다중 커서: ctrl+alt+위아래방향키
print(type(a))
print(type(b))
print(type(c))

# 다중 행 문자열(''', """)
x = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky."""
print(x)

y = "Twinkle, twinkle, little star,\
How I wonder what you are!\
Up above the world so high,\
Like a diamond in the sky."
print(y)

# 타입 변환
# int(), float(), str(), bool()
temperature = '20'
humidity = '50'
# 문자열 연결
print(temperature + humidity)

print(int(temperature) + int(humidity))

a = 0
b = 500
c = ''
d = '하하호호'
print(bool(a), bool(b), bool(c), bool(d))