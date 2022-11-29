class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr_num = None
        i = 0

        while i < len(nums):
            if nums[i] == curr_num:
                nums.pop(i)
                i -= 1
            else:
                curr_num = nums[i]
            i += 1

        return len(nums)
