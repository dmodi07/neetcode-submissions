class Solution:
    

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        first = strs[0]

        for k in range(len(first)):
            char = first[k]
            for s in strs[1:]:
                if k >= len(s) or s[k] != char:
                    return prefix  # mismatch or ran out of chars -> stop here
            prefix += char

        return prefix

            
