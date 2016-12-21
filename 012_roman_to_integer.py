"""
Author:     Wang, Fangyijie
Date:       Dec 21, 2016
Problem:    Roman to Integer
Difficulty: Easy
Source:     https://leetcode.com/problems/roman-to-integer/
Descriptions:
	Given a roman numeral, convert it to an integer.
	Input is guaranteed to be within the range from 1 to 3999.
"""

roman = {"M":1000,
				"D":500,
				"C":100,
				"L":50,
				"X":10,
				"V":5,
				"I":1}
sum = 0

for i in range(0,len(s)-1):
	if roman[s[i]] < roman[s[i+1]]:
		sum -= roman[s[i]]
	else:
		sum += roman[s[i]]

print sum + roman[s[-1]]

