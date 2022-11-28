class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        vals = []
        i = 1
        
        while i <= len(strs[0]):
            vals.append(strs[0][:i])
            i += 1

        if len(vals) == 0:
            return ""

        for i, v in enumerate(vals):
            for s in strs:
                print s[:i+1]
                if s[:i+1] != v:
                    if i is 0:
                        return ""
                    return vals[i-1]

        return vals[-1]