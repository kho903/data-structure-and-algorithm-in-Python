# 큐 (Queue)
- 자료(data element) 를 보관할 수 있는 (선형) 구조
- 단 넣을 때에는 한 쪽 끝에서 밀어 넣어야 하고<br>
-> 인큐(enqueue) 연산
- 꺼낼 때에는 반대 쪽에서 뽑아 꺼내야 하는 제약이 있음<br>
-> 디큐(dequeue) 연산
- 선입선출 (FIFO - First-In First-Out) 특징을 가지는<br>
  선형 자료 구조
  
## 큐의 동작
초기 상태 : 비어 있는 큐(empty queue)
```python
Q = Queue()
```
데이터 원소 A, B를 큐에 추가
```python
Q.enqueue(A)
Q.enqueue(B) # A 위에 B가 추가됨
r1 = Q.dequeue() # 데이터 원소 꺼내기 : A
r2 = Q.dequeue() # 데이터 원소 꺼내기 : B
```

## 큐의 추상적 자료구조 구현
### (1) 배열 (array)을 이용하여 구현
- Python 리스트와 메서드들을 이용
```python
class ArrayQueue:

    def __init__(self): # 빈 큐를 초기화
        self.data = []

    def size(self): # 큐의 크기를 리턴
        return len(self.data)

    def isEmpty(self): # 큐가 비어 있는 지를 판단
        return self.size() == 0

    def enqueue(self, item): # 데이터 원소를 추가
        self.data.append(item)

    def dequeue(self): # 데이터 원소를 삭제 (리턴)
        return self.data.pop(0)

    def peek(self): # 큐의 맨 앞 원소 반환
        return self.data[0]
```
- 연산 별 복잡도

| 연산 | 복잡도
|----------|:-------------
|size()|O(1)
|isEmpty()|O(1)
|enqueue()|O(1)
|dequeue()|O(n)
|peek()|O(1)


### (2) 연결 리스트 (linked list) 를 이용하여 구현
- 이전 강의에서 마련한 양방향 연결 리스트 이용

### 연산의 정의
- size() - 현재 큐에 들어 있는 데이터 원소의 수를 구함
- isEmpty() - 현재 큐가 비어 있는 지를 판단
- enqueue() - 데이터 원소 x를 큐에 추가
- dequeue() - 큐의 맨 앞에 저장된 데이터 원소를 제거 (또한, 반환)
- peek() - 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거하지 않음)