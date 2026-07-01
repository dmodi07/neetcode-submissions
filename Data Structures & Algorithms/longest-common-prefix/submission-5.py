class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        first = strs[0]

        for k in range(len(first)):
            char = first[k]
            for s in strs[1:]:
                if k >= len(s) or s[k] != char:
                    return string  
            string += char
        return string

            
