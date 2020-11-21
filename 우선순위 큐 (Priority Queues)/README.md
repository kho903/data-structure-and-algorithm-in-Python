# 우선순위 큐 (Priority Queue)
- 큐가 FIFO (First-In First-Out) 방식을 따르지 않고<br>
원소들의 우선순위에 따라 큐에서 빠져나오는 방식
- 작은 수가 우선순위가 높다고 가정<br>
Enqueue 6 7 3 2<br>
Dequeue 2 3 6 7
- 예 : 운영체제의 CPU 스케줄러 - 우선순위가 높은 작업을 먼저 큐에서 꺼내서 CPU를 할당해서 실행시키는 방식으로 동작
- 서로 다른 두 가지 방식이 가능:
    - (1) Enqueue 할 떄 우선순위 순서를 유지하도록
    - (2) Dequeue 할 때 우선순위 높은 것을 선택<br>
    
->어느 것이 더 유리할까? : 1번<br>
만약 큐에 우선순위에 상관없이 무작위로 늘어 서 있을 떄 Dequeue 할 떄 모든 데이터 원소를 다 살펴봐야 하기 때문

- 서로 다른 두 가지 재료를 이용할 수 있음 :
    - (1) 선형 배열 이용
    - (2) 연결 리스트 이용

-> 어느 것이 더 유리할까? : 연결 리스트<br>
Enqueue를 할 때 원소들을 우선순위에 따라 줄 지어 그 순서대로 유지해야되서 중간위치에 데이터를 삽입하는 경우가 빈번히 발생<br>
따라서, 선형배열을 이용하면 중간위치에 삽입 할 경우 뒤 원소들을 하나하나 전부 미뤄야 하지만 연결리스트를 이용할 경우 시간적 측면에서 더 유용
```python
from doublylinkedlist import Node, DoublLinkedList

class PriorityQueue:
    # 양방향 연결 리스트를 이용하여 빈 큐를 초기화
    def __init__(self):
        self.queue = DoublLinkedList()

    # 주의 : 양방향 연결 리스트의 
    # getAt() 메서드를 이용하지 않음!
    # 왜? : while문을 돌동안 계속해서 getAt()메서드가
    # node를 하나씩 세어나가는 것 방지
    def enqueue(self, x):
        newNode = Node(x)
        curr = ...
        while ... and ...:
            curr = curr.next
        self.queue....(curr, newNode)
```