class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    # 비어 있는 연결 리스트
    # of nodes : 0
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
