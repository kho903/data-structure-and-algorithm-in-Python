# 스택 (Stacks)
- 자료(data element) 를 보관 할 수 있는 (선형) 구조
- 단, 넣을 때에는 한 쪽 끝에서 밀어 넣어야 하고<br>
-> 푸시(push) 연산
- 꺼낼 때에는 같은 쪽에서 뽑아 꺼내야 하는 제약이 있음<br>
-> 팝(pop) 연산
- 후입선출(LIFO -> Last-In First-Out) 특징을 가지는 선형 자료구조

## 스택의 동작
- 초기 상태 : 비어 있는 스택 (empty stack)
- 데이터 원소 A를 스택에 추가 한 후 B도 추가

```python
S = Stack()
S.push(A)
S.push(B)
# 위에 있던 B가 꺼내져서 r1에 담김
r1 = S.pop() 
# 위에 있던 A가 꺼내져서 r2에 담김
r2 = S.pop() 
# 비어 있는 스택에서 데이터 원소를 꺼내려 할 떄
r3 = S.pop() # 스택 언더플로우(stack underflow) 오류
```

```python
# 꽉 찬 스택에 데이터 원소를 넣으려 할 떄
S = Stack()
S.push(A)
S.push(B)
S.push(C)
S.push(D)
S.push(E) # 스택 오버플로우 (stack overflow)
```

## 스택의 추상적 자료구조 구현


### 연산의 정의
- size() - 현재 스택에 들어 있는 데이터 원소의 수를 구함
- isEmpty() - 현재 스택이 비어 있는 지를 판단
- push(x) - 데이터 원소 x를 스택에 추가
- pop() - 스택의 맨 위에 저장된 데이터 원소를 제거 (또한, 반환)
- peek() - 스택의 맨 위에 저장된 데이터 원소를 반환 (제거하지 않음)

### 배열(array)을 이용하여 구현
- Python 리스트와 메서드들을 이용

```python
class ArrayStack:
    def __init__(self): # 빈 스택을 초기화
        self.data = []
    
    def size(self): # 스택의 크기를 리턴
        return len(self.data)
    
    def isEmpty(self): # 스택이 비어 있는 지 판단
        return self.size() == 0
    
    def push(self, item): # 데이터 원소를 추가
        self.data.append(item)
    
    def pop(self): # 데이터 원소를 삭제 (리턴)
        return self.data.pop()

    def peek(self): # 스택의 꼭대기 원소 반환
        return self.data[-1]
```

### 연결 리스트 (linked list)를 이용하여 구현
- 양방향 연결 리스트 이용

```python
from doublyLinkedList import Node
from doublyLinkedList import DoublyLinkedList

class LinkedListStack:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data
```


### 연습문제 -  수식의 괄호 유효성 겁사
1. 올바른 수식:
- (A + B)
- {(A + B) * C}
- [(A + B) * (C + D)]

2. 올바르지 않은 수식:
- (A + B
- A + B)
- {A * (B + C})
- [(A + B) * (C + D)}

#### 알고리즘 설계 - 수식을 왼쪽부터 한 글자씩 읽어서:
- 여는 괄호 - ( 또는 { 또는 [ - 를 만나면 스택에 푸시
- 닫는 괄호 - ) 또는 } 또는 ] - 를 만나면:<br>
    - 스택이 비어 있으면 올바르지 않은 수식<br>
    - 스택에서 pop, 쌍을 이루는 여는 괄호인지 검사<br>
        - 맞지 않으면 올바르지 않은 수식

