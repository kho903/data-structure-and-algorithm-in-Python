# 넓이 우선 순회 (breadth first traversal)
## 이진 트리의 순회 (Traversal)
- 깊이 우선 순회 (depth first traversal)
    - 중위 순회 (in-order traversal)
    - 전위 순회 (pre-order traversal)
    - 후위 순회 (post-order traversal)
- 넓이 우선 순회 (breadth first traversal)

## 넓이 우선 순회 (Breadth First Traversal)
- 원칙
    - 수준 (level) 이 낮은 노드를 우선으로 방문
    - 같은 수준의 노드들 사이에는, 
        - 부모 노드의 방문 순서에 따라 방문
        - 왼쪽 자식 노드를 오른쪽 자식보다 먼저 방문
- 재귀적(recursive) 방법이 적합한가? 

- 한 노드를 방문했을 때,
    - 나중에 방문할 노드들을 순서대로 기록해 두어야 <br>
      -> 큐(queue)를 이용하면 어떨까!


### 넓이 우선 순회 알고리즘 구현
```python
def BinaryTree:

    def bft(self):
        ...
```
1. (초기화) traversal <- 빈리스트, q <- 빈 큐
2. 빈 트리가 아니면, root node 를 큐에 추가 (enqueue)
3. q가 비어 있지 않은 동안<br>
    3.1 node <- q에서 원소를 추출 (dequeue)<br>
    3.2 node 를 방문
    3.3 node 의 왼쪽, 오른쪽 자식(있으면) 들을 q에 추가
4. q가 빈 큐가 되면 모든 노드 방문 완료