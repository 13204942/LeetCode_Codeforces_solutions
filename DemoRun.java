package com.demo.code;

public class DemoRun {

	public static void main(String[] args) {
		String str = "Hello pal lap olleH";
		String noStr = "Hello palindrome";
		
		DemoRun dr = new DemoRun();
		
//		dr.palindromeString(str);
//		dr.palindromeString(noStr);
		
		System.out.println(dr.reverseStr("hello I am here"));
		
	}
	
	public boolean palindromeString(String str) {
		
		int left = 0;
		int right = str.length() - 1;
		
		while(left < right) {
			
			if(str.charAt(left) == str.charAt(right)) {	
				left++;
				right--;				
			}else {
				System.out.println("The string is not palindrome");
				return false;
			}
		}
		System.out.println("The string is palindrome");		
		return true;
	}
	
	
	public String reverseStr(String str) {
		int left = 0;
		int right = str.length() - 1;
		char[] charArray = str.toCharArray();
		
		while(left < right) {
			char temp;
			temp = str.charAt(left);
			charArray[left] = charArray[right];
			charArray[right] = temp;
			left++;
			right--;
		}
		return new String(charArray);		
	}
}
