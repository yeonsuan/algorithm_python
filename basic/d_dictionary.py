# 리스트와 비슷하지만 요소와 key값이 매치되어있는 부분에서 다름.

a = {'name':'hong', 'age':24}
a['name'] # ==> 'hong'

a['height']=189 #요소 추가하기

del a['height'] #요소 삭제하기 del

a.keys() #key값만 가져오게 됨~ ['name','age']
a.values() #value값만~ ['hong',24]
a.items() #key, value값 같이 가져오게 됨!

a.clear() #모두 지우기