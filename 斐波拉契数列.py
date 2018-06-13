# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:27:27 2018

@author: ZJR

题目：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
"""


class Solution:
    def Fibonacci(self, n):
        # write code here
        fb = [0,1]
        if n < 2:
            return fb[n]
        else:
            for i in range(2,n+1):
                fb.append(fb[i-1]+fb[i-2])
        return fb[n]