class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2 * n) # Pre-allocate space for 2n elements
        
        for i in range(n):
            ans[i] = nums[i]        # Fill the first half
            ans[i + n] = nums[i]    # Fill the second half
            
        return ans
