"""
Author:     Wang, Fangyijie
Date:       Dec 21, 2016
Problem:    Arpa’s obvious problem and Mehrdad’s terrible solution
Difficulty: Easy
Source:     http://codeforces.com/problemset/problem/742/B
Descriptions:
	There are some beautiful girls in Arpa’s land as mentioned before.
	Once Arpa came up with an obvious problem:
	Given an array and a number x, count the number of pairs of indices i, j (1 ≤ i < j ≤ n) such that ai XOR aj = x, where XOR is bitwise xor operation (see notes for explanation).
	Immediately, Mehrdad discovered a terrible solution that nobody trusted. Now Arpa needs your help to implement the solution to that problem.
Input:
	First line contains two integers n and x (1 ≤ n ≤ 10^5, 0 ≤ x ≤ 10^5) — the number of elements in the array and the integer x.
	Second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 10^5) — the elements of the array.
Output:
	Print a single integer: the answer to the problem.
"""

n,x = map(int, raw_input().split())
r = 0
a = 200005*[0]

for k in map(int, raw_input().split()):
	r+=a[x^k]
	a[k]+=1
print r
