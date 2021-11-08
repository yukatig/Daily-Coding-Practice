"""
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.best = 0
        self.recursiveTree(root)
        return self.best - 1
        
    
    def recursiveTree(self, node):
        if node == None:
            return 0
        
        else:
            rightTree = self.recursiveTree(node.right)
            leftTree = self.recursiveTree(node.left)

            self.best = max(self.best, rightTree + leftTree + 1)
            
            return max(rightTree, leftTree) + 1

        