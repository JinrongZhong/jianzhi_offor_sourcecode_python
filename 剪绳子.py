# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:40:14 2018

@author: ZJR

题目：给你一根长度为n的绳子，请把绳子剪成m段（m,n）都是整数，
n>1并且m>1)每段绳子的长度记为k[0],k[1],k[2],...,k[m]。
请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度为2,3,3的三段，此时得到的最大乘积是18。
"""

'''
解法一：动态规划
定义 f(n) = k[0]*k[1]*...*k[m]。在剪第一刀的时候，我们有n-1种可能的选择，
也就是剪出来的第一段可能长度为1,2,3,...,n-1，因此，f(n) = max(f(i)*f(n-i)) 0<i<n
动态规划按照从下到上的顺序计算，即先计算f(2),f(3),再得到f(4),f(5),直到f(n)

当绳子长度为2时，只可能剪成长度都为1的两段，因此f(2) = 1
当绳子长度为3时，可以剪成（2,1）或者（1,1,1）,2*1>1*1*1,因此f(3)=2
'''

class Solution:
    def maxProductAfterCuting_Solution1(length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        
        products = [0,1,2,3]
        
        for i in range(4,length+1):
            Max = 0
            for j in range(1,i/2+1):
                product = products[j] * products[i-j]
                if Max < product:
                    Max = product    
            products[i] = Max
                    
        return products[length]
       
        
'''
解法二：贪婪算法
当n>5时，尽可能多的剪长度为3的绳子；当绳子剩下为4时，把绳子剪成两段长度为2的绳子。
当绳子长度n>5时， 3(n-3) > 2(n-2) > n， 因此要多剪长度为3的绳子段
'''    
class Solution2:
    def maxProductAfterCuting_Solution2(length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

    #尽可能多剪长度为3 的声字段
        timesOf3 = length/3
        
    #剩下绳子长度为4时，不能再剪长度为3
    #此时最好的方法是把绳子剪成长度为2的两段，因为2*2>3*1
        if length - timesOf3*3 == 1:
            timesOf3 -= 1
        
        timesOf2 = (length - timesOf3*3)/2
        return int(pow(3,timesOf3))*int(pow(2,timesOf2))
    
    

