# matrix-operations
Individual functions to implement matrix operations like add, subtract, split and print on n x n square matrices in Python can be found in matrix_operations.py. 

I provide three methods for multiplication of n x n square matrices 
1. Iteratively
2. Recursively
3. Strassen's method (split, perform operations on each split, then re-combine)

these can be found in
1. basic_matrix_multiply.py
2. matrix_multiply_recur.py
3. strassen.py

In matrix_comp.py there is a program that will evaluate all three methods on two identical 4 x 4 matrices and print the resulting matrix and the functions running time

in matrix.py I have implemented the same functions in an object oriented fashion where you can create a matrix object and pass it another matrix for operations
