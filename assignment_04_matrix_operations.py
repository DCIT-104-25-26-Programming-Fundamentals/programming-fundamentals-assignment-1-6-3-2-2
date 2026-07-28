# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix():
    matrix = []
    try:
        row_size = int(input("Enter number of rows: "))
        col_size = int(input("Enter number of columns: "))
        if (row_size or col_size) <= 0:
            print("Error: Please enter a positive integer.")
            
    except ValueError:
        print("Error: Invalid input")
        
    for i in range(1, row_size + 1):
        row = (input(f"Enter row {i}: ")).split(" ")
        row = [int(i) for i in row]
        matrix.append(row)
    
    return matrix
    
    
def write_matrix(matrix):
    for row in matrix:
        row = [str(x) for x in row]
        row = ' '.join(row)
        print(row)
        
    return
        
def transpose(matrix):
    
    final_matrix = []
    for col in range(len(matrix[0])):
        newRow =[]
        for row in range(len(matrix)):
            newRow.append((matrix[row])[col])
        final_matrix.append(newRow)
            
    return final_matrix

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("These matrices cannot be added because they have different sizes.")
        return
    final_matrix = []
    for row in range(len(matrix1)):
        newRow = []
        for col in range(len(matrix1[0])):
             element = matrix1[row][col]+matrix2[row][col]
             newRow.append(element)
        final_matrix.append(newRow)
    
    print("\n Sum: \n")   
    write_matrix(final_matrix)
    return
            
def multiply_matrices(matrix1,matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("These matrices cannot be multiplied because the number of columns of the first are not the same as the number of rows of the second.")
        return
    matrix2 = transpose(matrix2)
    final_matrix = []
    for row1 in range(len(matrix1)):
        newRow=[]
        for row2 in range(len(matrix2)):
            element = 0
            for col in range(len(matrix1[0])):
                element+=(matrix1[row1][col] * matrix2[row2][col])
            newRow.append(element)
        final_matrix.append(newRow)
    write_matrix(final_matrix)
    return 

print(f"Transposition of Matrices\n{'-' * 30}\n")
matrix = read_matrix()
print("\nTransposed Matrix: ")
write_matrix(transpose(matrix))
    
    
print(f"\nAddition of matrices\n{'-' * 30}\nFor matrix A:\n{'-' * 30}")
myMatrix1 = read_matrix()
print(f"\n{'-' * 30}\nFor matrix B:\n{'-' * 30}")
myMatrix2 = read_matrix()
add_matrices(myMatrix1,myMatrix2)

print(f"\nMultiplication of matrices\n{'-' * 30}\nFor matrix A:\n{'-' * 30}")
myMatrix1 = read_matrix()
print(f"\n{'-' * 30}\nFor matrix B:\n{'-' * 30}")
myMatrix2 = read_matrix()
multiply_matrices(myMatrix1,myMatrix2)