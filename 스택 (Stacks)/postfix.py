class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''
    for s in S:
        if s == '(':
            opStack.push(s)

        elif s in prec:
            if opStack.isEmpty():
                opStack.push(s)

            elif prec[opStack.peek()] >= prec[s]:
                while not opStack.isEmpty() and prec[opStack.peek()] >= prec[s]:
                    answer += opStack.pop()
                opStack.push(s)
            else:
                opStack.push(s)

        elif s == ')':
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        else:
            answer += s

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


a = solution("A+B+C")
print(a)
