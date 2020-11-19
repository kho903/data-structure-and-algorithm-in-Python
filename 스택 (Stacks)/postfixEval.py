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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for t in tokenList:
        if t == '(':
            opStack.push(t)
        elif t in prec:
            if opStack.isEmpty():
                opStack.push(t)
            elif prec[opStack.peek()] >= prec[t]:
                while not opStack.isEmpty() and prec[opStack.peek()] >= prec[t]:
                    postfixList.append(opStack.pop())
                opStack.push(t)
            else:
                opStack.push(t)

        elif t == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        else:
            postfixList.append(t)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        elif token == '*':
            x_result = valStack.pop() * valStack.pop()
            valStack.push(x_result)
        elif token == '/':
            sec = valStack.pop()
            fir = valStack.pop()
            devide_result = fir / sec
            valStack.push(devide_result)
        elif token == '+':
            plus_result = valStack.pop() + valStack.pop()
            valStack.push(plus_result)
        elif token == '-':
            sec = valStack.pop()
            fir = valStack.pop()
            minus_result = fir - sec
            valStack.push(minus_result)
    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
