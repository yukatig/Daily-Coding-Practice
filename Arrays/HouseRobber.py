class Solution: 
    def rob(self, nums: List[int]) -> int: 

        if not len(nums):
            return 0 

        if len(nums == 1):
            return nums[0]