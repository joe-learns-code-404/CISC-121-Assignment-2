def solution(A):
    # sort array
    A.sort()
    # every array should have at least one distinct value (exception of empty arrays)
    count = 1
    # index of array value we searching (gets changed)
    current = 0

    for x in range(len(A)): # 
        if A[current] != A[x]:
            count += 1
            current = x
    if len(A) == 0:
        return 0
    else:
        return count
