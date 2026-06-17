class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the next valid element's position

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move valid element forward
                k += 1             # Increment valid element count
                
        return k