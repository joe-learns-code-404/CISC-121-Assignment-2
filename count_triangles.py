A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].

[1, 2, 3, 4, 5]

def solution(A):
  A.sort()
  count = 0
  for i in range(len(A) - 2):
    k = i + 2
    for j in range(i + 1, len(A) - 1):
      while k < len(A) and A[i] + A[j] > A[k]:
        
