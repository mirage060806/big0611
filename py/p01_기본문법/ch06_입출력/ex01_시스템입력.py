# 시스템 입력
# input()
# 사용자로부터 이름을 터미널에 입력
'''
이름을 입력하세요: 홍길동
'''
name = input('이름을 입력하세요:')
# print(name)

print(name + "님, 안녕하세요")

# 키에 따른 권정체중
# input은 항상 문자열을 변환 -> int('170) -> 170
height = int(input('키를 입력하세요:'))
weight = (height - 100) * 0.9

print('권장 체중은 ' + str(weight) + 'kg 입니다')