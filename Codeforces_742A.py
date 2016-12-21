"""
Author:     Wang, Fangyijie
Date:       Dec 21, 2016
Problem:    Arpa’s hard exam and Mehrdad’s naive cheat
Source:     http://codeforces.com/problemset/problem/742/A
Descriptions:
	There exists an island called Arpa’s land, some beautiful girls live there, as ugly ones do.
	Mehrdad wants to become minister of Arpa’s land. Arpa has prepared an exam. Exam has only one question, given n, print the last digit of 1378n.
	Mehrdad has become quite confused and wants you to help him. Please help, although it's a naive cheat.
Input:
	The single line of input contains one integer n (0  ≤  n  ≤  10^9).
Output:
	Print single integer — the last digit of 1378^n.
"""

out = [8,4,2,6]
n = int(input())
if n==0:
	print 1
else:
	print out[n%4-1]