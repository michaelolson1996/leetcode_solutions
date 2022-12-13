class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        i = 0
        rom_str = ""

        num_vals = [
            1000,
            900,
            500,
            400,
            100,
            90,
            50,
            40,
            10,
            9,
            5,
            4,
            1,
        ]

        rom_vals = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        while i < 13:
            if num - num_vals[i] >= 0:
                rom_str += rom_vals[i]
                num -= num_vals[i]
            else:
                i += 1

        return rom_str
