# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:06:20 2018

@author: ZJR

题目：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？


"""
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold <= 0 or rows <= 0 or cols <=0 :
            return 0
        
        visited = [0]*rows*cols
        count = self.movingCountCore(threshold, rows,cols,0,0,visited)
        
        return count
    
    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row*cols + col] = 1
            count = (1 + self.movingCountCore(threshold, rows, cols, row-1, col, visited)
                + self.movingCountCore(threshold, rows, cols, row + 1, col, visited)
                + self.movingCountCore(threshold, rows, cols, row, col - 1, visited)
                + self.movingCountCore(threshold, rows, cols, row, col + 1, visited))
        return count

    #check函数用来判断机器人是否能进入坐标为（row,col）的格子   
    def check(self, threshold, rows, cols, row, col, visited):
        if (row >= 0 and col >= 0 and row < rows and col < cols 
            and visited[row*cols + col] == 0 
            and self.getDigitSum(row) + self.getDigitSum(col) <= threshold ):
            return True
        return False
    
    #getDigitSum得到一个数字的位数之和   
    def getDigitSum(self,number):
        Sum = 0 
        while number >0:
            Sum += number%10
            number /= 10
            print number,Sum
        return Sum
            
            


         