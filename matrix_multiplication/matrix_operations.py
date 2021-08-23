# combines four sub matrices representing the values of
# quadrant 2, 1, 3 and 4, respectively
def combine_matrix(A, B, C, D):

    n = len(A) * 2 # output matrix for matrices n x n size will be 2n x 2n
    # create ampty output matrix
    Z = [[0 for y in range(n)] for x in range (n)]

    # Fit the four matrices into the larger output matrix

    half = n // 2

    for i in range(half):
        for j in range(half):
            Z[i][j] = A[i][j]

    for i in range(half):
        for j in range(half, n):
            Z[i][j] = B[i][j-half]

    for i in range(half, n):
        for j in range(half):
            Z[i][j] = C[i-half][j]

    for i in range(half, n):
        for j in range(half, n):
            Z[i][j] = D[i-half][j-half]

    return Z


# Adds two matrices together
# assumes matrices are sqaures of equivalent size
# to allow for addition
def add_matrix(A, B):

    n = len(A)

    C = [[0 for y in range(n)] for x in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]

    return C

# subtracts first matrix from second
# assumes matrices are sqaures of equivalent size
# to allow for subtraction
def subtract_matrix(A, B):
    
    n = len(A)

    C = [[0 for y in range(n)] for x in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]

    return C

# Splits matrix into four sub matrices of equal size
def matrix_split(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    new_rows = rows // 2 # to index halfway through
    new_cols = cols // 2

    C11 = [matrix[i][:new_cols] for i in range(new_rows)]
    C12 = [matrix[i][new_cols:] for i in range(new_rows)]
    C21 = [matrix[i][:new_cols] for i in range(new_rows, rows)]
    C22 = [matrix[i][new_cols:] for i in range(new_rows, rows)]

    return C11, C12, C21, C22

def print_matrix(matrix):

    for row in matrix:
        matrix_row = ""
        for col in row:
            element = str(col) + " "
            matrix_row += element
        print(matrix_row)

