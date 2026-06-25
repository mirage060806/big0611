# 비효율적인 방법
fruit1 = 'apple'
fruit2 = 'banana'
fruit3 = 'orange'

# 컨테이너 자료형
# : 리스트, 튜플, 세트, 딕셔너리
# 효율적인 방법
fruits = ['apple', 'banana', 'orange']
print(fruits)

fruits2 = ['apple', 'banana', 'orange', 'apple', 'banana']
print(fruits2)

# 아이템 선택
# 인덱싱
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
# 슬라이싱
print(fruits[1:3])

# 수정(Update)
fruits[1] = 'kiwi'
print(fruits)

# 추가
# 객체.insert(인덱스, 아이템): 인덱스에 추가
fruits.insert(2, 'mango')
print(fruits)

# 객체.append(아이템): 끝에 추가
fruits.append('watermalon')
print(fruits)

# 리스트1.extend(리스트2)
vagetables = ['carror', 'tomato', 'onion']
fruits.extend(vagetables)
print(fruits)

# + 연산
list1 = [1, 2, 3]
list2 = ['가', '나', '다']
print(list1 + list2)

# 삭제
# 리스트.remove(아이템)
fruits.remove('tomato')
print(fruits)
# del 리스트[인덱스]
del fruits[-1]
print(fruits)
# del 리스트
del fruits
# print(fruits)
# NameError

fruits = ['사과', '키위', '망고']
print(fruits)
# 리스트.clear(): 리스트의 아이템만 모두 삭제
fruits.clear()
print(fruits)

# 정렬(sort)
'''
- 오름차순: 
1, 2, 3,...
a, b, c,...
가, 나, 다,...

- 내림차순(역, reverse):
3, 2, 1, -1,...
c, b, a
다, 나, 가
'''
fruits = ['딸기', '망고', '블루베리', '수박', '사과', '바나나', '오렌지']
print("정렬전:", fruits)
# 리스트.sort(): 오름차순
fruits.sort()
print("정렬전:", fruits)

# 리스트.sort(reverse = True): 내림차순
fruits.sort(reverse = True)
print(fruits)