class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = "aeiou"
        vowels_count = { "a": 0, "b": 0 }
        cutoff = len(s) / 2

        for i in range(0, len(s)):
            if i < cutoff and lower(s[i]) in vowels:
                vowels_count["a"] += 1
            elif lower(s[i]) in vowels:
                vowels_count["b"] += 1

        return vowels_count["a"] == vowels_count["b"]
