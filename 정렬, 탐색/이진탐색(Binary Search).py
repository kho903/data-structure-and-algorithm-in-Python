# 탐색하려는 리스트가 이미 정렬되어 있는 경우에만 적용 가능
# 크기 순으로 정렬되어 있다는 성질 이용
# 한 번 비교가 일어날 때마다 리스트를 반씩 줄임
# O(log n)


def solution(L, x):
    answer = -1
    lower = 0
    upper = len(L) - 1

    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            return middle
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1

    return answer


L = [1, 2, 3, 4, 5, 6, 7, 9]
a = solution(L, 9)
print(a)
