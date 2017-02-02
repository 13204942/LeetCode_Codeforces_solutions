"""
Author:     Wang, Fangyijie
Date:       Feb 02, 2017
Problem:    Isomorphic Strings
Difficulty: Easy
Source:     https://leetcode.com/problems/isomorphic-strings/
Descriptions:
    Given two strings s and t, determine if they are isomorphic.
    Two strings are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters. 
    No two characters may map to the same character but a character may map to itself.
Example:
    Given "egg", "add", return true.
    Given "foo", "bar", return false.
    Given "paper", "title", return true.
Note:
    You may assume both s and t have the same length.
Hint:
    Python zip, map, set
"""

"""
TOP SOLUTION (Python):
def isIsomorphic(self, s, t):
    f = lambda s: map({}.setdefault, s, range(len(s)))
    return f(s) == f(t)

Description:
    https://discuss.leetcode.com/topic/14315/1-liner-in-python/2
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        return len(set(zip(s,t)))==len(set(s))==len(set(t))
        """
        if len(set(zip(s,t)))==len(set(s))==len(set(t)):
            return True
        else:
            return False
 