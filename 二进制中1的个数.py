# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:10:08 2018

@author: ZJR

题目：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
"""

class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum([(n>>i & 1) for i in range(0,32)])
