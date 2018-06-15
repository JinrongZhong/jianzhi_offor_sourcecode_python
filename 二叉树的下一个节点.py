# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:23:16 2018

@author: ZJR

题目：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


解题思路：
1. 如果该节点有右子树，那么它的下一个节点就是它的右子树中的最左子节点
2. 如果该节点没有右子树，且它是它父节点左子节点，那么它的下一个节点就是它的父节点
3. 如果该节点没有右子树，且它是它父节点的右子节点，那就沿着它的父节点的指针向上遍历，
直到找到一个是它父节点的左子节点的节点，如果这样的节点存在，那么它的父节点就是我们要找的下一个节点。

"""

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        
        if pNode.right:
            pLeft = pNode.right
            while pLeft.left:
                pLeft = pLeft.left
            return pLeft
        elif pNode.next:
            pParent = pNode.next
            pCurrent = pNode
            while pParent and pParent.right == pCurrent:
                pCurrent = pParent
                pParent = pParent.next
            return pParent