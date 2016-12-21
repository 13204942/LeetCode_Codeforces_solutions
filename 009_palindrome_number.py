"""
Author:     Wang, Fangyijie
Date:       Dec 21, 2016
Problem:    Palindrome Number
Difficulty: Easy
Source:     https://leetcode.com/problems/palindrome-number/
Descriptions:
	Determine whether an integer is a palindrome. Do this without extra space.
"""

x = -5454
copy_x = x
rev_x = 0
l = []
lv = []

"""
if x>=0 and int(str(x)[::-1]) == x:
	print True
else:
	print False


if x == 0:
	print True
elif x > 0:	
	while x > 0.1:
		l.append(int(x%10))
		x = int(x/10)

	for i in range(0, len(l)):
		rev_x += l[i]*10**(len(l)-i-1)

	if copy_x == rev_x:
		print True
	else:
		print False
else:
	print False
"""

if x == 0:
	print True
elif x > 0:	
	while x > 0.1:
		rev_x = rev_x*10 + int(x%10)
		x = int(x/10)

	if copy_x == rev_x:
		print True
	else:
		print False
else:
	print False