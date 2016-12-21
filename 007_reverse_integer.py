"""
Author:     Wang, Fangyijie
Date:       Dec 21, 2016
Problem:    Reverse Integer
Difficulty: Easy
Source:     https://leetcode.com/problems/reverse-integer/
Descriptions:
	Reverse digits of an integer.
	Example1: x = 123, return 321
	Example2: x = -123, return -321
"""

sx = str(x)
r = 0
if sx[0] != '-':
	r = int(sx[::-1])
elif x == 0:
    r = 0
else:
	r = int('-'+sx[1:len(sx)][::-1])

if (r > 2147483647) or (r < -2147483648):
    return 0
else:
    return r