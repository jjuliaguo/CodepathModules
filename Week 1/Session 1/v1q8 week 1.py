#Question 8:
# 
# Write a function local_maximums() that accepts an n x n integer matrix grid 
# and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

# local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid 
# centered around row i + 1 and column j + 1.

# In other words, we want to find the largest value in every contiguous 3 x 3 matrix 
# in grid.

"""
Understand:

Question: can we assume that n x n > 3x3
Valid when the middle number of 3 is the largest local_maxes[i][j]
Hardcode: the 3x3 matrix that is centered (fixed)
Within 3x3, find the largest value and assign it to local maxes array
- > think abt how to store index for the local_maxes (variables or no?)

Returns an (n-2) x (n-2) matrix 


"""

def local_maximums(grid):
	smallerRow = 0
    smallerCol = 0
    result = []

    for row in range(0, len(grid)-2): #should be -2 because 4-3 = 1 but 1 not included
        for col in range(0, len(grid[0])-2):
             temp2d = grid[]

# Example Usage:

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
print(local_maximums(grid))
# Example Output:

# [[9, 9], [8, 6]]
# [[2, 2, 2], [2, 2, 2], [2, 2, 2]]