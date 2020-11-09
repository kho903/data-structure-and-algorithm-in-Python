# 조합의 수 계산
# 문제 : n개의 서로 다른 원소에서 m개를 택하는 경우의 수
from math import factorial as f


def combi(n, m):
    return f(n) / (f(m) * f(n - m))


def combi2(n, m):
    # 효율성 측면 좋지 않음
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        return combi2(n - 1, m) + combi2(n - 1, m - 1)


a = combi(3, 1)
print(a)


# 연습문제
# 재귀적 이진탐색
def binsearch(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return binsearch(L, x, l, mid - 1)
    else:
        return binsearch(L, x, mid + 1, u)
