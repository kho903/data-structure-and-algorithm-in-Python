# 배열 - 정렬 (sort) 과 탐색 (search)
## Python 리스트의 정렬
### sorted()
- 내장 함수(built-in function)
- 정렬된 새로운 리스트를 얻어냄
### sort()
- 리스트의 메서드(method)
- 해당 리스트를 정렬함
#### 정렬의 순서를 반대로
- reverse=True
- L2 = sorted(L, reverse=True)
- L.sorted(reverse=True)

#### 정렬 - 문자열로 이루어진 리스트의 경우
정렬 순서는 사전 순서 (알파벳 순서)를 따름
(문자열 길이가 긴 것이 더 큰 것이 아님)
- 문자열 길이 순서로 정렬하려면?<br>
-> 정렬에 이용하는 키(key)를 지정<br>

예) 
```
>>> L = ['abcd', 'xyz', 'spam'] 
>>> sorted(L, key=lambda x: len(x))
['xyz', 'abcd', 'spam']
>>> L = ['spam', 'xyz', 'abcd']
>>> sorted(L, key=lambda x: len(x))
['xyz', 'spam', 'abcd']
```

#### 키를 지정하는 또 다른 예
```
L = [{'name' : 'John', 'score' : 83}, {'name' : 'Paul', 'score' : 92}]
L.sort(key=lambda x: x['name'])
# 레코드들을 점수 높은 순으로 정렬
```
# 탐색알고리즘 (1) - 선형 탐색(Linear Search)
리스트의 길이에 비례하는 시간 소요<br>
-> O(n)<br>
최악의 경우 : 모든 원소를 다 비교해 보아야

# 탐색알고리즘 (2) - 이진 탐색(Binary Search)
한 번 비교가 일어날 때마다 리스트 반씩 줄임<br>
(divide & conquer)<br>
-> O(log n)