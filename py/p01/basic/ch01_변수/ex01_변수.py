# 변수
a = 5
# 수학식 '='
a == 5
print(a)

b = 3
print(b)

print(a + b)

# 문자열
c = '가나다'
print(c)

radio_freq = 107.9
print(radio_freq)

# 잘못된 변수명:

# 숫자로 시작
# 2var = '숫자'

# 공백 포함
# happy var = '공백'

# 특수 문자 포함 (_ 제외)
# happyvar! = '특수문자'

# 예약어 사용
# def = '함수'

# 대소문자 구별
abc = 5
ABC = 'Apple'
# 내장함수의 인자의 수는 제한 없다
print(abc, ABC)

# -----------------------------

# 다중 변수 동시 선언
x, y, z = 'Apple', 'Banana', 'Carrot'
print(x, y, z)

# 변수명에 _ 사용
# 주로 사용하지 않을 변수를 위한 자리표시자로 사용.
_, var = 3, 5
print(_, var)
add = _ + var
print(add)

# 단일 갑의 다중 변수 할당
x = y = z = '같은값'
print(x, y, z)