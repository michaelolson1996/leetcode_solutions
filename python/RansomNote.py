class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        available_letters = {}

        for letter in magazine:
            if available_letters.has_key(letter):
                available_letters[letter] += 1
            else:
                available_letters[letter] = 1

        for letter in ransomNote:
            if available_letters.has_key(letter) and available_letters[letter] > 0:
                available_letters[letter] -= 1
            else:
                return False

        return True
