# -*- coding: utf-8 -*-
"""
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。


str.strip([chars]) 返回移除字符串头尾指定的字符生成的新字符串。
默认为空格

Created on Wed May 16 21:46:55 2018

@author: ZJR
"""




class Solution:
    # s 源字符串
    def replaceSpace_v1(self, s):
        # write code here
        if len(s) != 0:  
            s.replace(' ', '%20')            
        return s
    
    def replaceSpace_v2(self, s):
        res = ''
        for ele in s:
            if ele == ' ':
                res += '%20'
            else:
                res += ele
        return res
    def replaceSpace_v3(self, s):
        res = ''
        for ele in s:
            if ele.strip():
                res += ele
            else :
                res += '%20'
        return res
    
    def replaceSpace_v4(self, s):
        s = list(s)
        for i in range(len(s)):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)


   
String = 'We Are Happy.'
print type(String)
S = Solution()
s = S.replaceSpace_v4(String)
print s    
