class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max1 = 0
        if len(nums) == 1:
            return nums[0]
            
        for i in nums:
            max2 = 0
            for j in nums[1:]:
                if i == j:
                    max2 += 1
                if max2 > max1:
                    return i