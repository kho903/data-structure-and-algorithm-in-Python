# exprStr: 중위표현식으로 된 수식
def splitTokens(exprStr):
    # 피연산자와 연산자로 갈라서 tokens에 담음
    tokens = []
    # 수를 만났을 떄, 자리수별로 더해주기 위함
    # 예 : 23을 만나면 처음에 2를 만나면 val에 2 저장,
    # 3을 만나면 2* 10 + 3 으로 23 저장
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