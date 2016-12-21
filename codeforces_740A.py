"""
Author:     Wang, Fangyijie
Date:       Dec 21, 2016
Problem:    Alyona and copybooks
Source:     http://codeforces.com/problemset/problem/740/A
Descriptions:
	Little girl Alyona is in a shop to buy some copybooks for school. She study four subjects so she wants to have equal number of copybooks for each of the 
	subjects. There are three types of copybook's packs in the shop: it is possible to buy one copybook for a rubles, a pack of two copybooks for b rubles, and a 
	pack of three copybooks for c rubles. Alyona already has n copybooks.
	What is the minimum amount of rubles she should pay to buy such number of copybooks k that n + k is divisible by 4? There are infinitely many packs of any type 
	in the shop. Alyona can buy packs of different type in the same purchase.
Input:
	The only line contains 4 integers n, a, b, c (1 ≤ n, a, b, c ≤ 10^9).
Output:
	Print the minimum amount of rubles she should pay to buy such number of copybooks k that n + k is divisible by 4.
"""

n,a,b,c = raw_input().split( )

int_n = int(n) 
int_a = int(a)
int_b = int(b)
int_c = int(c)

if int_n%4 == 1:
	print min(3*int_a, int_c, int_a+int_b)
elif int_n%4 == 2:
	print min(2*int_a, int_b, 2*int_c)
elif int_n%4 == 3:
	print min(int_a, 3*int_c, int_b+int_c)
else:
	print 0