"""
Author:     Wang, Fangyijie
Date:       Feb 21, 2017
Problem:    Happy Number
Difficulty: Easy
Source:     https://leetcode.com/problems/happy-number/?tab=Description
Descriptions:
    Write an algorithm to determine if a number is 'happy'.
    A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its
    digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
    Those numbers for which this process ends in 1 are happy numbers.
Example:
    19 is a happy number
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
Credits:
    Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.
"""

public class Solution {
    public boolean isHappy(int n) {
        while(n>1) {
            int x = split(n);
            if(x==1) {
                return true;
            }
            if((x%10)==5) {
                return false;
            }
            n = x;
        }
        return true;
    }
    public int split(int num) {
        int s = 0;
        while(num>0) {
            s = s + (num%10)*(num%10);
            num = num/10;
        }
        return s;
    }
}