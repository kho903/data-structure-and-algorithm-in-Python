class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal = []
        q = ArrayQueue()
        if self.root:
            q.enqueue(self.root)

        while q.isEmpty() == False:
            a = q.dequeue()
            traversal.append(a.data)
            if a.left:
                q.enqueue(a.left)
            if a.right:
                q.enqueue(a.right)
        return traversal
    
    # 시행착오 q.enqueue()를 할떄 .data 를 쓰지 말 것

def solution(x):
    return 0


