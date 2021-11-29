"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
        currNode = head
        values = []
        while(currNode):
            values.append(currNode.val)
            currNode = currNode.next
            
        changeNode = head 
        for i in range(len(values)):
            changeNode.val = values[len(values) - 1 - i]
            changeNode = changeNode.next
        return head
    
        #alternate:
        """
        curr = head 
        prev = None
        nextNode = None
        while(curr):
            nextNode = curr.next
            curr.next = prev 
            prev = curr
            curr = nextNode

        return prev
        """