'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        result = []
        curr = []
        self.backtrack(s, curr, result)
        return result
    
    def isPalindrome(self, s):
        return s == s[::-1]
        
    def backtrack(self, s, curr, result):
        if not s:
            result.append(curr)
        else:
            for i in range(1, len(s) + 1):
                left = s[0:i]
                right = s[i:len(s)]
                if self.isPalindrome(left):
                    self.backtrack(right, curr+[left], result)
            