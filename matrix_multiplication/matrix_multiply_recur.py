import matrix_operations

# Multiply two n x n square matrices in On^2 time complexity
def matrix_multiply_recur(A, B):

    n = len(A) # Set n

    if n == 1: # base case of 1 digit matrix
        D = [[0]]
        D[0][0] = A[0][0] * B[0][0]
        return D

    else:

        # Split the initial two matrices into four sub matrices recursively until
        # they hold only a single value
        A11, A12, A21, A22 = matrix_operations.matrix_split(A)
        B11, B12, B21, B22 = matrix_operations.matrix_split(B)

        # Add the sub matrices together such that they represent
        # each quadrant of the output matrix
        C11 = matrix_operations.add_matrix(matrix_multiply_recur(A11, B11), matrix_multiply_recur(A12, B21))

        C12 = matrix_operations.add_matrix(matrix_multiply_recur(A11, B12), matrix_multiply_recur(A12, B22))

        C21 = matrix_operations.add_matrix(matrix_multiply_recur(A21, B11), matrix_multiply_recur(A22, B21))

        C22 = matrix_operations.add_matrix(matrix_multiply_recur(A21, B12), matrix_multiply_recur(A22, B22))

        # stack the four output sub matrices horizontally and vertically
        C = matrix_operations.combine_matrix(C11, C12, C21, C22)

    return C

"""
test = [[1, 2, 1, 2],
        [1, 2, 1, 2],
        [1, 2, 1, 2],
        [1, 2, 1, 2]]


test2 = test

print(test)
print(test2)

result = matrix_multiply_recur(test, test2)
print(result)
"""
