class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0

        if x <= 1:
            return x

        while i < x + 1:
            if i * i > x:
                return i - 1
            elif i * i == x:
                return i
            i += 1
