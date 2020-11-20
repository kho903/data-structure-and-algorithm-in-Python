# 큐(Queue) 의 활용
- 자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적으로 (asynchronously) 일어나는 경우
- 자료를 생성하는 작업이 여러 곳에서 일어나는 경우
- 자료를 이용하는 작업이 여러 곳에서 일어나는 경우
- 자료를 생성하는 작업과 그 자료를 이용하는 작업이 양쪽 다 여러 곳에서 일어나는 경우
- 자료를 처리하여 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야 하는 작업의 경우

## 환형 큐 (Circular Queue)
- 정해진 개수의 저장 공간을 빙 돌려가며 이용
```python
Q.enqueue(A)
Q.enqueue(B)
Q.enqueue(C)
r1 = Q.dequeue() # A
Q.enqueue(D)
r2 = Q.dequeue() # B
# 데이터를 꺼내는 쪽 : front
# 데이터를 집어 넣는 쪽 : rear
```
- 큐가 가득 차면?<br>
-> 더이상 원소를 넣을 수 없음 (큐 길이를 기억하고 있어야 함)

## 환형 큐의 추상적 자료구조 구현
###연산의 정의
- size() : 현재 큐에 들어 있는 데이터 원소의 수를 구함
- isEmpty() : 현재 큐가 비어 있는 지를 판단
- ifFull() : 큐에 데이터 원소가 꽉 차 있는 지를 판단
- enqueue() : 데이터 원소 x를 큐에 추가
- dequeue() : 큐의 맨 앞에 저장된 데이터 원소를 제거 (또한, 반환)
- peek() : 큐의 맨 앞에서 저장된 원소를 반환 (제거하지 않음)

## 배열로 구현한 환형 큐
- 정해진 길이 n (예에서는 6)의 리스트를 확보해 두고
```python
Q.enqueue(A) # 0번 인덱스 A <- rear
Q.enqueue(B) # 1번 인덱스 B <- rear
Q.enqueue(C) # 2번 인덱스 C <- rear
Q.enqueue(D) # 3번 인덱스 D <- rear
r1 = Q.dequeue() # 0번 인덱스 A <- front , r1 = A
r2 = Q.dequeue() # 1번 인덱스 B <- front , r2 = B
Q.enqueue(E) # 4번 인덱스 E <- rear
Q.enqueue(F) # 5번 인덱스 F <- rear
# A, B 를 dequeue 했기 때문에 full인 상태는 아니다 따라서 enqueue() 가능
Q.enqueue(G) # 0번 인덱스 G <- rear
r3 = Q.dequeue() # 2번 인덱스 C <- rear , r3 = C 
```
- front와 rear를 적절히 계산하여 배열을 환형으로 재활용

```python
class CircularQueue:

    def __init__(self, n):
        # 빈 큐를 초기화
        # 인자로 주어진 최대 큐 길이 설정
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        # 현재 큐 길이를 반환
        return self.count

    def isFull(self):
        # 큐가 꽉 차 있는가?
        return self.count == self.maxCount

    def enqueue(self, x):
        # 큐에 데이터 원소 추가
        if self.isFull():
            raise IndexError('Queue full') # exception 으로 처리
        self.rear = ...
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        # 큐에서 데이터 원소 뽑아내기
        if ...:
           raise IndexError("Queue empty")
        self.front = ...
        x = ...
        self.count -= 1
        return x 
    
    def peek(self):
        # 큐의 맨 앞 원소 들여다 보기
        if ...:
            raise IndexError('Queue empty')
        return ...
```
- circularQueue.py 에서 문제해결 내용 적음