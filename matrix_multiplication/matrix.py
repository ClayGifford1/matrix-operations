import copy

class Matrix:
    def __init__(self, array):
        self.matrix = copy.deepcopy(array)

    # prints each row of the matrix on a subsequent line
    def print_matrix(self):

        for row in self.matrix:
            matrix_row = ""
            for col in row:
                element = str(col) + " "
                matrix_row += element
            print(matrix_row)


    # combines four sub matrices representing the values of
    # quadrant 2, 1, 3 and 4, respectively
    def combine_matrix(self, A, B, C, D):

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
    def add_matrix(self, A, B = []):

        if (len(B) == 0):

            B = self.matrix

        n = len(A)

        C = [[0 for y in range(n)] for x in range(n)]

        for i in range(n):
            for j in range(n):
                C[i][j] = A[i][j] + B[i][j]

        return C


    # subtracts first matrix from second
    # assumes matrices are sqaures of equivalent size
    # to allow for subtraction
    def subtract_matrix(self, A, B = []):

        if (len(B) == 0):
    
            B = self.matrix
        
        n = len(A)

        C = [[0 for y in range(n)] for x in range(n)]

        for i in range(n):
            for j in range(n):
                C[i][j] = A[i][j] - B[i][j]

        return C


    # Splits matrix into four sub matrices of equal size
    def matrix_split(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        new_rows = rows // 2 # to index halfway through
        new_cols = cols // 2

        C11 = [matrix[i][:new_cols] for i in range(new_rows)]
        C12 = [matrix[i][new_cols:] for i in range(new_rows)]
        C21 = [matrix[i][:new_cols] for i in range(new_rows, rows)]
        C22 = [matrix[i][new_cols:] for i in range(new_rows, rows)]

        return C11, C12, C21, C22


    # multiply two n x m matrices in On^3 time completixy
    def basic_matrix_multiply(self, B):

        rows = len(self.matrix) # set n
        cols = len(B[0]) # set m
        # create a new matrix to hold the output
        C = [[0 for y in range(cols)] for x in range(rows)]

        # Loop through the two matrices and multiply them
        # storing the results in the output matrix
        for x in range(rows):
            for y in range(cols):
                for z in range(len(B)):
                    C[x][y] += self.matrix[x][z] * B[z][y]
        return C


    # Multiply two n x n square matrices in On^2 time complexity
    def matrix_multiply_recur(self, A, B = []):

        if(len(B) == 0):

            B = self.matrix

        n = len(A) # Set n

        if n == 1: # base case of 1 digit matrix
            D = [[0]]
            D[0][0] = A[0][0] * B[0][0]
            return D

        else:

            # Split the initial two matrices into four sub matrices recursively until
            # they hold only a single value
            A11, A12, A21, A22 = self.matrix_split(A)
            B11, B12, B21, B22 = self.matrix_split(B)

            # Add the sub matrices together such that they represent
            # each quadrant of the output matrix
            C11 = self.add_matrix(self.matrix_multiply_recur(A11, B11), self.matrix_multiply_recur(A12, B21))

            C12 = self.add_matrix(self.matrix_multiply_recur(A11, B12), self.matrix_multiply_recur(A12, B22))

            C21 = self.add_matrix(self.matrix_multiply_recur(A21, B11), self.matrix_multiply_recur(A22, B21))

            C22 = self.add_matrix(self.matrix_multiply_recur(A21, B12), self.matrix_multiply_recur(A22, B22))

            # stack the four output sub matrices horizontally and vertically
            C = self.combine_matrix(C11, C12, C21, C22)

        return C


    # uses strassens method of matrix multiplication to reduce time complexity
    # to O(n^lg7)
    def strassen(self, B):

        n = len(self.matrix) # Set n

        if n == 1: # base case of 1 digit matrix
            D = [[0]]
            D[0][0] = self.matrix[0][0] * B[0][0]
            return D

        else:

            # create four sub matrices for each matrix
            A11, A12, A21, A22 = self.matrix_split(self.matrix)
            B11, B12, B21, B22 = self.matrix_split(B)

            # create ten matrices containing various addition and subtractions
            S1 = self.subtract_matrix(B12, B22)
            S2 = self.add_matrix(A11, A12)
            S3 = self.add_matrix(A21, A22)
            S4 = self.subtract_matrix(B21, B11)
            S5 = self.add_matrix(A11, A22)
            S6 = self.add_matrix(B11, B22)
            S7 = self.subtract_matrix(A12, A22)
            S8 = self.add_matrix(B21, B22)
            S9 = self.subtract_matrix(A11, A21)
            S10 = self.add_matrix(B11, B12)

            # recursively multiply various matrices
            P1 = self.matrix_multiply_recur(A11, S1)
            P2 = self.matrix_multiply_recur(S2, B22)
            P3 = self.matrix_multiply_recur(S3, B11)
            P4 = self.matrix_multiply_recur(A22, S4)
            P5 = self.matrix_multiply_recur(S5, S6)
            P6 = self.matrix_multiply_recur(S7, S8)
            P7 = self.matrix_multiply_recur(S9, S10)

            # generate four sub matrices
            C11 = self.add_matrix(self.subtract_matrix(self.add_matrix(P5, P4), P2), P6)
            C12 = self.add_matrix(P1, P2)
            C21 = self.add_matrix(P3, P4)
            C22 = self.subtract_matrix(self.subtract_matrix(self.add_matrix(P5, P1), P3), P7)

            # combine to form output matrix
            C = self.combine_matrix(C11, C12, C21, C22)

            return C
