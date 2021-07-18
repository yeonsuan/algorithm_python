#간단 파이썬
#리스트
a = [1,2,'apple','banana']
b = [1,2,['apple','banana']] #리스트안에 또 리스트 넣기
c = [1,2,('apple','banana')] #괄호안은 튜플이라는건데..

#인덱싱
a=['apple','banana','orange']
print(a[1:3]) #여기서 왜 3일까? index는 요소자체가 아니라 자리를 의미.

#comprehension
a = [x*2 for x in range(6)] #여기서 for x in range(6)은 반복문
print(a)

#zip() 세로로 묶어주는거 ..?
a = [1,2,3]
b = [4,5,6]
e = list(zip(a,b))
print(e)