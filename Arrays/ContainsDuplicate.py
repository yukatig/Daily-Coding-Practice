class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        for num in nums:
            if count.has_key(num):
                return True
            else:
                count[num] = 1

        return False
