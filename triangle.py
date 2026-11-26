def solution(A):
  # search through three sections of the array at once
    for x in range(len(A)):
        for y in range(x + 1, len(A)):
            for z in range(y + 1, len(A)):
                if A[x] + A[y] > A[z] and A[y] + A[z] > A[x] and A[z] + A[x] > A[y]:
                    # the moment even one trangle triplet is found, stop loops and return 1
                    return 1
    # if nothing is a triangle, then return 0
    return 0
