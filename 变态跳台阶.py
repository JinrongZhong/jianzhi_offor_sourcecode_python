# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:09:11 2018

@author: ZJR

题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。

"""

class Solution:
    def jumpFloorII(self, number):
        # write code here
        result = [0,1,2]
        if number < 3:
            return result[number]
        if number >= 3:
            for i in range(3,number+1):
                temp = 1
                for j in range(0,i):
                    temp += result[j]
                result.append(temp)
