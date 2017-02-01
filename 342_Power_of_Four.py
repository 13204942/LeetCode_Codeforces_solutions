"""
Author:     Wang, Fangyijie
Date:       Feb 01, 2017
Problem:    Power of Four
Difficulty: Easy
Source:     https://leetcode.com/problems/power-of-four//
Descriptions:
    Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Example:
    Given num = 16, return true. Given num = 5, return false.
Follow up: 
    Could you solve it without loops/recursion?
"""

"""
TOP SOLUTION (Python):
def isPowerOfFour(self, num):
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num

Description:
    Any other number not it the list should be considered as invalid.
    So if you XOR them altogether, you will get a mask value, which is:

    1010101010101010101010101010101 (1431655765)
    Any number which is power of 4, it should be power of 2, I use num &(num-1) == 0 to make sure of that.
    Obviously 0 is not power of 4, I have to check it.
    and finally I need to check that if the number 'AND' the mask value is itself, to make sure it's in the list above.
"""

class Solution(object):
    def isPowerOfFour(self, num):
        couZero = str(bin(num)[3:]).count('0')
        couOne = str(bin(num)[3:]).count('1')
        if(num==0):
            return False
        elif(num==1):
            return True
        elif(couZero % 2 ==0 and couOne == 0 ):
            return True
        else:
            return False