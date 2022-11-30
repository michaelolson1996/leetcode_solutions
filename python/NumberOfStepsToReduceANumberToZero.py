class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """

        i = 0

        while num > 0:
            if num == 1:
                num = 0
            elif num % 2 == 0:
                num = num / 2
            elif num % 2 == 1:
                num = num - 1
            
            i = i + 1

        return i
