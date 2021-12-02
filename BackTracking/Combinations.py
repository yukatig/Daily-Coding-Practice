"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        nums = []
        for i in range(n):
            nums.append(i + 1)

        self.helper(nums, k, [], result)
        return result

    def helper(self, nums, k, temp, result):

        if k == 0:
            if temp not in result:
                result.append(temp)
            return

        for i in range(len(nums) - k + 1):
            self.helper(nums[i + 1:], k - 1, temp + [nums[i]], result)
