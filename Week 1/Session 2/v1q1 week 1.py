# Question 1: Transpose Matrix
# 
# Write a function transpose() that accepts a 2D integer array matrix 
# and returns the transpose of matrix. The transpose of a matrix is the 
# matrix flipped over its main diagonal, swapping the rows and columns.

#3x3 matrix before and after being transposed


def transpose(matrix):
    #python good for string manipulation
    #built in function?

    #use a for loop to iterate through the rows and then columns
    #
    pass

#Example Usage

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))

#Example Output:

#[
   # [1, 4, 7],
   # [2, 5, 8],
  #  [3, 6, 9]
# ]
# [
   # [1, 4],
  #  [2, 5],
  #  [3, 6]
#]