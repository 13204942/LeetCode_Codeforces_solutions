"""
Author:     Wang, Fangyijie
Date:       Jun 30, 2017
Problem:    136. Single Number 
Difficulty: Easy
Source:     https://leetcode.com/problems/single-number/
Descriptions:
  	Given an array of integers, every element appears twice except for one. Find that single one.
Note:
		Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 
"""

"""
My solution:
"""
#nums.sort()
#if len(nums) == 1:
#	print nums[0]
#else:
#	for i in range(0, len(nums), 2):
#		if nums[i] != nums[i+1]:
#			print nums[i]
#			break
#		elif i == len(nums)-3:
#			print nums[-1]
#			break


"""
Best solution:
"""
ans =0

for num in nums:
	ans ^= num
print ans