def solution(A):
    # empty array to store each sum
    sums = []

    for x in range(len(A)):
        for y in range(len(A)):
            # add all pairings together and store their absolute values in the sums array
            sums.append(abs(A[x] + A[y]))
    # sort the sums array so the min value is at the front
    sums.sort()
    return sums[0]
