class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        add_checks = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        sub_checks = { "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900 }
        count = 0
        i = 0

        while i < len(s):
            if i is not len(s) - 1 and s[i] + s[i+1] in sub_checks:
                count += sub_checks[s[i] + s[i+1]]
                i += 1
            else:
                count += add_checks[s[i]]
            i += 1
            
        return count