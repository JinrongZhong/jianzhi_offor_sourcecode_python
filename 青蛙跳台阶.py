# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:43:54 2018

@author: ZJR

题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

class Solution:
    def jumpFloor(self, number):
        # write code here
        result = [1,2,3]
        if number <= 3:
            return result[number-1]
        if number >= 3:
            for i in range(3,number):
                result.append(result[i-1]+result[i-2])
        return result[number-1]