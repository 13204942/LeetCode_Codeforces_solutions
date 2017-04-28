"""
Author:     Wang, Fangyijie
Date:       Apr 28, 2017
Problem:    557. Reverse Words in a String III  
Difficulty: Easy
Source:     https://leetcode.com/problems/reverse-words-in-a-string-iii/#/description
Descriptions:
	Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Example:
	Input: "Let's take LeetCode contest"
	Output: "s'teL ekat edoCteeL tsetnoc"
Note:
	In the string, each word is separated by single space and there will not be any extra space in the string. 
"""

// Java Solution
public class Solution {
    public String reverseWords(String s) {
        char[] in=s.toCharArray();
    	int j=0;
    	for(int i=0; i<in.length; i++) {
    		if(in[i]==' ') {
    			reverseChar(in, j, i-1);
    			j=i+1;
    		}
    	}
    	reverseChar(in, j, in.length-1);
    	return new String(in);
    }
    public void reverseChar(char[] c, int begin, int end) {
        while(end>begin){
            char temp = c[begin];
            c[begin]=c[end];
            c[end] = temp;
            end--;
            begin++;
        }
    }
}

// Python Solution
//def reverseWords(self, s):
//	return ' '.join(s.split()[::-1])[::-1]