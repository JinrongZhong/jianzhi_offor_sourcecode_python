# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:35:23 2018

@author: ZJR

题目： 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，
 但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
 路径不能再次进入该格子。
 
 
解题思路：由于回溯法的递归特性，路径可以被看成一个栈。当矩阵中定位了路径中前n个字符的位置后，
在于第n个字符对应的格子周围（上下左右）都没有找到第n+1个字符，这时候只好在路径上返回到第n-1个字符，重新定位第n个字符
"""
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if len(matrix)== 0 and rows < 0  and cols < 0  and len(path) ==0:
            return False
        
        visited = [0]*rows*cols
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
               if self.hasPathCore(matrix,rows,cols,row,col,path,pathLength,visited):
                   return True
        return False

    def hasPathCore(self,matrix,rows,cols,row,col,path,pathLength,visited):
        if pathLength == len(path):
            return True
        hasPath = False
        if (row >= 0 and row < rows and col >= 0 and col < cols 
            and path[pathLength] == matrix[row*cols + col] 
            and visited[row*cols + col] ==0) :
            pathLength += 1
            visited[row*cols +col] = 1
            
            hasPath = (self.hasPathCore(matrix,rows,cols,row,col-1,path,pathLength,visited)
                or self.hasPathCore(matrix,rows,cols,row,col+1,path,pathLength,visited)
                or self.hasPathCore(matrix,rows,cols,row-1,col,path,pathLength,visited)
                or self.hasPathCore(matrix,rows,cols,row+1,col,path,pathLength,visited))
            
            if not hasPath:
                visited[row*cols + col] = 0
                pathLength -= 1
                
        return hasPath
            
                
            
