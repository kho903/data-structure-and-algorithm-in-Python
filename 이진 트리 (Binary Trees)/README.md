# 이진 트리의 추상적 자료구조
## 연산의 정의
- size() - 현재 트리에 포함되어 있는 노드의 수를 구함
- depth() - 현재 트리의 깊이(또는 높이; height)를 구함
- 순회 (traversal)

## 이진 트리의 구현 - 노드 (Node)
- 노드에는 data 아이템 뿐만 아니라 left child, right child 하나씩 가질 수 있다.
- Node
    - Data
    - Left Child
    - Right Child

```python
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
```

## 이진 트리의 구현 - 트리 (Tree)
- root 노드만 가리키고 있으면 그 다음은 각각의 노드들이 간선으로 연결됨
```python
class BinaryTree:
    def __init__(self, r):
        self.root = r
```

## 이진 트리의 구현 - size()
- 재귀적인 방법으로 쉽게 구할 수 있다.
```python
class Node:

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

class BinaryTree:

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0
```
## 이진 트리의 구현 - depth()
- 재귀적인 방법으로 쉽게 구할 수 있다.
- 전체 이진트리의 depth()<br>
    = left subtree 의 depth() 와 right subtree의 depth()<br>
    중 더 큰 것 + 1
```python
class Node:
    def depth(self):
        ...

class BinaryTree:
    def deptg(self):
        if ...
```

## 이진 트리의 순회 (Traversal)
- 깊이 우선 순회 (depth first traversal)
    - 중위 순회(in-order traversal)
    - 전위 순회(pre-order traversal)
    - 후위 순회(post-order traversal)
- 넓이 우선 순회 (breadth first traversal)

### 중위 순회 (In-order Traversal)
- 순회의 순서
    - (1) Left subtree
    - (2) 자기 자신
    - (3) Right subtree
```python
class Node:

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal +=self.right.inorder()
        return traversal

class BinaryTree:

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
```

### 전위 순회 (Pre-order Traversal)
- 순회의 순서:
    - (1) 자기자신
    - (2) Left subtree
    - (3) Right subtree
    
### 전위 순회 (Pre-order Traversal)
- 순회의 순서:
    - (1) Left subtree
    - (2) Right subtree
    - (3) 자기자신
    