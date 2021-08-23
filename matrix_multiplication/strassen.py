import matrix_operations
import matrix_multiply_recur 

# uses strassens method of matrix multiplication to reduce time complexity
# to O(n^lg7)
def strassen(A, B):

    n = len(A) # Set n

    if n == 1: # base case of 1 digit matrix
        D = [[0]]
        D[0][0] = A[0][0] * B[0][0]
        return D

    else:

        # create four sub matrices for each matrix
        A11, A12, A21, A22 = matrix_operations.matrix_split(A)
        B11, B12, B21, B22 = matrix_operations.matrix_split(B)

        # create ten matrices containing various addition and subtractions
        S1 = matrix_operations.subtract_matrix(B12, B22)
        S2 = matrix_operations.add_matrix(A11, A12)
        S3 = matrix_operations.add_matrix(A21, A22)
        S4 = matrix_operations.subtract_matrix(B21, B11)
        S5 = matrix_operations.add_matrix(A11, A22)
        S6 = matrix_operations.add_matrix(B11, B22)
        S7 = matrix_operations.subtract_matrix(A12, A22)
        S8 = matrix_operations.add_matrix(B21, B22)
        S9 = matrix_operations.subtract_matrix(A11, A21)
        S10 = matrix_operations.add_matrix(B11, B12)

        # recursively multiply various matrices
        P1 = matrix_multiply_recur.matrix_multiply_recur(A11, S1)
        P2 = matrix_multiply_recur.matrix_multiply_recur(S2, B22)
        P3 = matrix_multiply_recur.matrix_multiply_recur(S3, B11)
        P4 = matrix_multiply_recur.matrix_multiply_recur(A22, S4)
        P5 = matrix_multiply_recur.matrix_multiply_recur(S5, S6)
        P6 = matrix_multiply_recur.matrix_multiply_recur(S7, S8)
        P7 = matrix_multiply_recur.matrix_multiply_recur(S9, S10)

        # generate four sub matrices
        C11 = matrix_operations.add_matrix(matrix_operations.subtract_matrix(matrix_operations.add_matrix(P5, P4), P2), P6)
        C12 = matrix_operations.add_matrix(P1, P2)
        C21 = matrix_operations.add_matrix(P3, P4)
        C22 = matrix_operations.subtract_matrix(matrix_operations.subtract_matrix(matrix_operations.add_matrix(P5, P1), P3), P7)

        # combine to form output matrix
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

result = strassen(test, test2)

print(result)
"""