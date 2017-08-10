package com.demo.code;

public class FloodFill {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FloodFill ff = new FloodFill();
		int initialRange[][] = new int[][]{
										  { 0, 1, 0, 0, 0, 0, 0, 0, 1, 1 },
										  { 1, 1, 1, 1, 0, 1, 0, 0, 1, 0 },
										  { 0, 0, 1, 1, 1, 1, 0, 0, 1, 0 },
										  { 0, 0, 0, 0, 1, 1, 1, 1, 1, 0 },
										  { 0, 0, 0, 0, 1, 0, 0, 1, 0, 0 }
										};
										
//		System.out.println(initialRange[0].length);
		int x = 1;
		int y = 1;
		int newColor = 2;
		ff.floodEntry(initialRange, x, y, newColor);
		for(int m=0; m < 5; m++) {
			for(int n=0; n < 10; n++) {
				System.out.print(initialRange[m][n]);
			}
		}
	}
	
	public void floodEntry(int[][] range, int x, int y, int newColor) {
		int curColor = range[x][y];
		flood(range, x, y, curColor, newColor);
	}
	
	public void flood(int[][] range, int x, int y, int curColor, int newColor) {
		if(x < 0) return;
		if(y < 0) return;
		if(x > range.length-1) return;
		if(y > range[x].length-1) return;
		
		if(range[x][y] != curColor) {
			return;
		}else {
			range[x][y] = newColor;
			
			flood(range,x+1,y,curColor,newColor);
			flood(range,x-1,y,curColor,newColor);
			flood(range,x,y+1,curColor,newColor);
			flood(range,x,y-1,curColor,newColor);
		};
	}

}
