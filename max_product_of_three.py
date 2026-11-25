def solution(A):
    # empty array to store each product
    products = []

    for x in range(len(A)):
        for y in range(x + 1, len(A)):
            for z in range(y + 1, len(A)):
                # multiply all groupings together and store their values in the products array
                products.append(A[x] * A[y] * A[z])
    # sort the sums array so the min value is at the front and max is at end
    products.sort()
    return products[len(products) - 1]
