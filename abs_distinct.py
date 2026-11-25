def solution(A):
    # change every variable to it's absolute value
    for i in range(len(A)):
        A[i] = abs(A[i])
    # sort array
    A.sort()
    # every array should have at least one distinct value (exception of empty arrays)
    count = 1
    # index of array value we searching (gets changed)
    current = 0

    for x in range(len(A)): # look through array
        if A[current] != A[x]: # another distinct variable is found
            count += 1 # count value goes up
            current = x
    if len(A) == 0: # if array is empty
        return 0
    else:
        return count

