# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:13:46 2018

@author: ZJR


题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""

class Solution1:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        else:
            Min = rotateArray[0]
            for i in range(1,len(rotateArray)):
                if rotateArray[i] < Min:
                    Min = rotateArray[i]
                    break
            return Min
        
        
        
class Solution2:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        else:
            index1 = 0
            index2 = len(rotateArray) - 1
            indexMid = index1
            while(rotateArray[index1] >= rotateArray[index2]):
                if (index2 - index1) == 1:
                    indexMid = index2
                    break
                indexMid = (index1+ index2)/2
                if rotateArray[index1]==rotateArray[index2] and rotateArray[index1]==rotateArray[indexMid]:
                    return self.MinInOrder(rotateArray)
                elif rotateArray[index1] <= rotateArray[indexMid]:
                    index1 = indexMid
                elif rotateArray[index2] >= rotateArray[indexMid]:
                    index2 = indexMid
        return rotateArray[indexMid]
  
    def MinInOrder(self,rotateArray):
        Min = rotateArray[0]
        for i in range(1,len(rotateArray)):
            if rotateArray[i] < Min:
                Min = rotateArray[i]
                break
        return Min