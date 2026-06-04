#Given an array nums with n integers, write a function non_decreasing() that checks if nums 
# could become non-decreasing by modifying at most one element.

#We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) 
# such that (0 <= i <= n - 2).

def non_decreasing(nums):
	for index in range(len(nums) - 2):
		if 
#Example Usage:

nums = [4, 2, 3]
non_decreasing(nums)

nums = [4, 2, 1]
non_decreasing(nums)
#Example Output:

#True
#False