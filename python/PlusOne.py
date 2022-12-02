class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        count = ""

        for i in digits:
            count += str(i)

        new_count = str(int(count) + 1)

        for i in new_count:
            i = int(i)


        return new_count
