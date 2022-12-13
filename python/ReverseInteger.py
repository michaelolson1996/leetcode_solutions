class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > 0:
            new_num = int(str(x)[::-1])
            if new_num > 2**31 - 1:
                return 0
            else:
                return new_num
        elif x < 0:
            new_num = int("-" + str(x)[1:][::-1])
            if new_num < -2**31:
                return 0
            else:
                return new_num
        else:
            return 0
