"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        indexDict = {}
        result = []
        
        for i in range(len(nums)):
            containsElm = indexDict.has_key(nums[i])
            if containsElm:
                newKey = indexDict.get(nums[i])
                newKey.append(i)
                indexDict[nums[i]] = newKey
            else:
                indexDict[nums[i]] = [i]
            
        for key in indexDict:
            dif = target - key 
            containsDif = indexDict.has_key(dif)
            
            if dif == key:
                return indexDict.get(key)
            
            keyIndex = indexDict.get(key)
            difIndex = indexDict.get(dif)
            
            if (containsDif):
                result.append(keyIndex[0])
                result.append(difIndex[0])
                break
                
        return result
        """
        indexDict = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if indexDict.has_key(diff):
                return [indexDict.get(diff), i]
            indexDict[nums[i]] = i