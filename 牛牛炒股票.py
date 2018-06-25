# -*- coding: utf-8 -*-
"""

题目：牛牛得知了一些股票今天买入的价格和明天卖出的价格，他找犇犇老师借了一笔钱，现在他想知道他最多能赚多少钱。
输入描述:
每个输入包含一个测试用例。
输入的第一行包括两个正整数,表示股票的种数N(1<=N<=1000)和牛牛借的钱数M(1<=M<=1000)。
接下来N行，每行包含两个正整数，表示这只股票每一股的买入价X(1<=X<=1000)和卖出价Y(1<=Y<=2000)。
每只股票可以买入多股，但必须是整数。
输出描述:
输出一个整数表示牛牛最多能赚的钱数。
示例1
输入
3 5 
3 6 
2 3 
1 1
输出
4
Created on Wed May 23 19:43:02 2018

@author: ZJR
"""

import sys
import numpy as np

def isLegal(x,lower,upper):
    if x.isdigit() and int(x) >= lower and  int(x) <= upper:
        return True
    else:
        return False

N,M = raw_input().split(' ')
if isLegal(N,1,1000) and isLegal(M,1,1000):
    mark = np.array([[0,0,0],[0,0,0],[0,0,0]])
    count = 0
    N,M = map(int, [N,M ])
    for i in range(0,N):
        X,Y = raw_input().split(' ')
        if isLegal(X,1,1000) and isLegal(Y,1,1000):
            X,Y = map(int, [X,Y])
            mark[i][0] = X
            mark[i][1] = Y
            mark[i][2] = Y-X
        else:
            sys.exit()
    mark= mark[np.lexsort(-mark.T)]
    if M > mark[0][0]:
        
        count += M/mark[0][0]*mark[0][2]
        M = M % mark[0][0]         
        print count ,M
    if M > mark[1][0]:        
        count += M/mark[1][0]*mark[1][2]
        M = M % mark[1][0]
        print count,M
    if M > mark[2][0]:
        count += M/mark[2][0]*mark[2][2]
        M = M % mark[2][0]
        
    print count 
    print mark    
else:
    sys.exit()