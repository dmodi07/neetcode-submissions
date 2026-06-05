class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        temp = 0

        for i in nums:
            if (i == 1):
                temp += 1
                max_count = max(temp, max_count)
            else:
                temp = 0

        return max_count