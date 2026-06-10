#Question 5: Missing Clues
# 
# Christopher Robin set up a scavenger hunt for Pooh, 
# but it's a blustery day and several hidden clues have blown away. 

# Write a function find_missing_clues() to help Christopher Robin figure out 
# which clues he needs to remake. The function accepts two integers lower and upper 
# and a unique integer array clues. All elements in clues are 
# within the inclusive range [lower, upper].

#A clue x is considered missing if x is in the range [lower, upper] and x is not 
# in clues.

#Return the shortest sorted list of ranges that exactly covers all the 
# missing numbers. That is, no element of clues is included in any of 
# the ranges, and each missing number is covered by one of the ranges.

def find_missing_clues(clues, lower, upper):
	result = []
	tempArr = []

	clues.sort()

	for i in range(len(clues) -1): #len==5 then 0,1,2,3
		""" The last index case:
		if i == len(clues) -2: #so if len == 5, it would be at 3
			lowerBound = clues[i+1] + 1
			tempArr = [lowerBound, upper]
			result.append(tempArr) """
		
		if clues[i+1] - clues[i] > 1:
			upperBound = clues[i+1] - 1
			lowerBound = clues[i] + 1
			tempArr = [lowerBound, upperBound]
			result.append(tempArr)
		
	#this part has to be outside the loop since we want to check the last clue 
	# with the upper bound
	if clues[-1] < upper: #REMEMBER: -1 is the last index here
		result.append([clues[-1] + 1, upper])
	
	return result
		
"""
Checking for the previous alg:

for i in range of 0 to 4: (0,1,2,3)

i==0:
if 0 == 3: no
elif 1-0 == 1: no

i==1:
if 1 == 3: no
elif 3-1 == 2: yes
upperBound = 2
lowerBound = 2
tempArr = [2, 2]
result = [[2, 2]]

i==2:
if 2 == 3: no
elif 50-3 == 47: yes
upperBound = 49
lowerBound = 4
tempArr = [4, 49]
result = [[2, 2], [4, 49]]

i==3:
if 3 == 3: yes
lowerBound = 76
tempArr = [76, 99]
result = [[2, 2], [4, 49], [76, 99]] -> couldn't figure out why [76, 99] replaced [4, 49]


"""
# Example Usage:

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))

#Example Output:

#[[2, 2], [4, 49], [51, 74], [76, 99]]

""" Explanation of first output:
Range: 0 - 99 (inclusive)

The missing numbers:
2
4, 5, 6, ..., 49
51, 52, ..., 74
76, 77, ..., 99

Now group into ranges:

[2, 2]      # only 2 is missing
[4, 49]     # 4 through 49 are missing
[51, 74]    # 51 through 74 are missing
[76, 99]    # 76 through 99 are missing
"""

#[]