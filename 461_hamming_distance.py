"""
Author:     Wang, Fangyijie
Date:       Dec 21, 2016
Problem:    Hamming Distance
Difficulty: Easy
Source:     https://leetcode.com/problems/hamming-distance/
Descriptions:
	The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
	Given two integers x and y, calculate the Hamming distance.
Note:
	0 ≤ x, y < 2^31.
Example:
	Input: x = 1, y = 4

	Output: 2

	Explanation:
	1   (0 0 0 1)
	4   (0 1 0 0)
	       ↑   ↑
	The above arrows point to positions where the corresponding bits are different.
"""

"""
x = 3
y = 1
out = 0
kx = []
ky = []
while x > 0:
	ax = int(x%2)
	x = int(x/2)
	kx.append(ax)

while y > 0:
	ay = int(y%2)
	y = int(y/2)
	ky.append(ay)

if len(kx) == max(len(kx), len(ky)):	
	for i in range(0, len(kx)-len(ky)):
		ky.append(0)
else:
	for i in range(0, len(ky)-len(kx)):
		kx.append(0)

for j in range(0, len(kx)):
	if kx[j] != ky[j]:
		out += 1

print out, kx[::-1], ky[::-1]
"""

x = 3
y = 1

print "{0:b}".format(x^y).count("1")
