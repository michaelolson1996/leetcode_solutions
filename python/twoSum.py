    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for idx in range(0, len(nums)):
            sec_val = target - nums[idx]
            for sec_idx in range(idx + 1, len(nums)):
                if nums[sec_idx] == sec_val:
                    return [idx, sec_idx]