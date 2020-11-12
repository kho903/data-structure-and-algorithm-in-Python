# 양방향 연결 리스트 (Doubly Linked Lists)
- 한 쪽으로만 링크를 연결하지 말고, 양쪽으로!<br>
-> 앞으로도 (다음 node) 뒤로도 (이전 node) 진행 가능
- Node의 구조 확장<br>
```python
class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None
```

- 리스트 처음과 끝에 dummy node를 두자!<br>
-> 데이터를 담고 있는 node 들은 모두 같은 모양

```python
class DoublyLinkedList:
    def __init__(self, item):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
```

## 리스트 순회
```python
def traverse(self):
    result = []
    curr = self.head
    while curr.next.next:
        curr = curr.next
        result.append(curr.data)
    return result
```

## 리스트 역순회
```python
def reverse(self):
    result = []
    curr = self.tail
    while curr.prev.prev:
        curr = curr.prev
        result.append(curr.data)
    return result
```

## 원소의 삽입
*L.insertAfter(prev, newNode)*
```python
def inserttAfter(self, prev, newNode):
    next = prev.next
    newNode.prev = prev
    newNode.next = next
    prev.next = newNode
    next.prev = newNode
    self.nodeCount += 1
    return True
```

## 특정 원소 얻어 내기
- 지난 번 것과 동일
```python
def getAt(self, pos):
    if pos < 0 or pos > self.nodeCount:
        return None
    i = 0
    curr = self.head
    while i < pos:
        curr = curr.next
        i += 1
    return curr
```

## 원소의 삽입 (getAt 이용)
*L.insertAt(pos, newNode)
```python
def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
        return False

    prev = self.getAt(pos - 1)
    return self.insertAfter(prev, newNode)
```
-> 리스트 마지막에 원소 삽입하면??? - 앞에서 부터 찾아가므로 오래걸림<br>
- 따라서, getAt 함수를 조금 수정한다.
```python
def getAt(self, pos):
    if pos < 0 or pos > self.nodeCount:
        return None

    if pos > self.nodeCount // 2:
        i = 0
        curr = self.tail
        while i < self.nodeCount - pos + 1:
            curr = curr.prev
            i += 1
    else:
        ...
```

### 연습문제 - 양방향 연결리스트 메서드 구현
- def insertBefore(self, next, newNode)<br><br>
- def popAfter(self, prev)
- def popBefore(self, next)
- def popAt(self, pos)<br><br>
- def concat(self, L)