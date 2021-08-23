# multiply two n x m matrices in On^3 time completixy
def basic_matrix_multiply(A, B):

    rows = len(A) # set n
    cols = len(B[0]) # set m
    # create a new matrix to hold the output
    C = [[0 for y in range(cols)] for x in range(rows)]

    # Loop through the two matrices and multiply them
    # storing the results in the output matrix
    for x in range(rows):
        for y in range(cols):
            for z in range(len(B)):
                C[x][y] += A[x][z] * B[z][y]
    return C

"""
test = [[1, 2],
        [3, 4],
        [5, 6]]

test2 = [[1, 2, 3],
        [4, 5, 6]]

result = basic_matrix_multiply(test, test2)

print(test)
print(test2)
print(result)

test3 = [[1, 2, 1, 2],
        [1, 2, 1, 2],
        [1, 2, 1, 2],
        [1, 2, 1, 2]]

test4 = test3

result = basic_matrix_multiply(test3, test4)
print(test3)
print(test4)
print(result)
"""