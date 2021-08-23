import matrix_operations
import basic_matrix_multiply
import matrix_multiply_recur
import strassen
import time

# function to check the running time of each method
# starts a timer just before the function executes
# and ends it right after
def matrix_time_check(func, A, B):
    start = time.perf_counter()
    C = func(A, B)
    end = time.perf_counter()

    final = end - start
    matrix_operations.print_matrix(C)
    print("\nRunning time - {}".format(final))

A = [[2, 2, 2, 2],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
    [2, 2, 2, 2]]

B = A

print("""

This program will show how different methods affect 
the running time of the process for 2-dimensional 
n x n square matrix multiplication

                    3 methods will be used

1. Iterative multiplication 
2. Recursive multiplication
3. Strassen's method

""")

print("Matrices to multiply:")

print("\nMatrix A\n")
matrix_operations.print_matrix(A)

print("\nMatrix B\n")
matrix_operations.print_matrix(B)

print("\nResults of A x B\n")

print("\nIterative Method\n")
func = basic_matrix_multiply.basic_matrix_multiply
matrix_time_check(func, A, B)

print("\nRecursive Method\n")
func = matrix_multiply_recur.matrix_multiply_recur
matrix_time_check(func, A, B)

print("\nStrassen's Method\n")
func = strassen.strassen
matrix_time_check(func, A, B)
