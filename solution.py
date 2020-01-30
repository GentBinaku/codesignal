def solution(A):
    n = len(A)
    result = 0
    for i in range(n - 1):
        if (A[i] == A[i + 1]):
            result = result + 1
    r = 0
    for i in range(n):
        count = 0
        A[i] = 1 - A[i]
        for j in range(n - 1):
            if (A[j] == A[j + 1]):
                count = count + 1
        r = max(r, count)
        A[i] = A[i] + 1
    return result + r


print solution([1,1,0,1,0,1])