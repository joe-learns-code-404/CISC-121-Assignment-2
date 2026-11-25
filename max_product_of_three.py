def solution(A):
    # empty array to store each product
    products = []

    for x in range(len(A)):
        for y in range(x + 1, len(A)):
            for z in range(y + 1, len(A)):
                products.append(A[x] * A[y] * A[z])
    products.sort()
    return products[len(products) - 1]
