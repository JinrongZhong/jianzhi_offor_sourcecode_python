# -*- coding: utf-8 -*-
"""
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这
样的一个二维数组和一个整数，判断数组中是否含有该整数。

解题思路：
选取右上角的数字arr[0][column-1]与target进行比较,arr[0][column-1] 是第0行最大第column列最小
arr[0][column-1] > target 则第column-1列元素均比target大，剔除第column-1列，保留剩下的row行column-1列进行查找
arr[0][column-1] < target 则第0行元素均比target小，剔除第0列，保留剩下的row-1行column列进行查找
......
依次类推，直到右上角数字与target相等，返回True;否则，返回False


Created on Tue May 15 19:47:33 2018

@author: ZJR
"""

from numpy import array

a = array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
print len(a)


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array)!=0:
            row = len(array)-1
            column = 0
            while row >= 0 and column < len(array[row]):
                if array[row][column] == target:
                    return True
                elif array[row][column] > target:
                    row -= 1
                else:
                    column += 1
            return False
        

S = Solution()
print S.Find(7,a)



