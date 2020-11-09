# 재귀함수 (recursive functions) 란?
# 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것
# 생각보다 많은 종류의 문제가 재귀적으로 해결 가능

# 예
# 이진 트리(binary trees)
# 왼쪽 서브트리의 원소들은 모두 작거나 같을 것
# 오른쪽 서브트리의 원소들은 모두 클것
# 이 원칙을 모든 노드에 적용

# 보다 간단한 예
# 자연수의 합 구하기
# 문졔: 1부터 n까지 모든 자연수의 합을 구하시오.
def sum_recursive(n):
    # 재귀 호출의 종결 조건
    # 시간 복잡도 O(n)
    if n <= 1:
        return n
    else:
        return n + sum(n - 1)


def sum_iterative(n):
    # 시간 복잡도 O(n)
    s = 0
    while n >= 0:
        s += n
        n -= 1
    return s


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(x):
    if x <= 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


a = int(input("Number: "))
print(sum_recursive(a))
