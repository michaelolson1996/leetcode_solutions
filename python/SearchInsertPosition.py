class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for i in range(len(nums)):
            if nums[i] == target or target < nums[i]:
               return i
            elif nums[i] > target and nums[i + 1] < target:
                return i + 1
            elif i == len(nums) - 1:
                return i + 1
