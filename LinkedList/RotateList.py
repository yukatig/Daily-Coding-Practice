"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
       
        #edge case 0
        if head == None:
            return None
        
        #find the length
        length = 1
        followingNode = head
        while followingNode.next != None:
            followingNode = followingNode.next
            length += 1
            
        #modulo k
        k = k % length
        
        #make circlular linked list
        followingNode.next = head
        
        #pointer to length - k in circular linked list
        node = head
        for i in range(length - k - 1):
            node = node.next
            
        #break circular list 
        answer = node.next
        node.next = None
        
        return answer