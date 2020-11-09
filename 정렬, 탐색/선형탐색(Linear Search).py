def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1


L = [2, 4, 3, 7, 0, 10]

a = linear_search(L, 1)
print()
