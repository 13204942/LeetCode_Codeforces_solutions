"""
Author:     Wang, Fangyijie
Date:       Apr 24, 2017
Problem:    Array Partition I 
Difficulty: Easy
Source:     https://leetcode.com/problems/array-partition-i/#/description
Descriptions:
    Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible. 
Example:
		Input: [1,4,3,2]
		Output: 4
		Explanation: n is 2, and the maximum sum of pairs is 4.
Note:
    n is a positive integer, which is in the range of [1, 10000].
    All the integers in the array will be in the range of [-10000, 10000].
"""

public class Solution {
    public int arrayPairSum(int[] nums) {

        Arrays.sort(nums);
        int sum = 0;
        
        for(int i = 0; i < nums.length-1; i = i+2) {
            sum = sum + nums[i];
        }
        
        return sum;
    }
}