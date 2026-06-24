class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    next_greater = -1
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            next_greater = nums2[k]
                            break
                    lst.append(next_greater)
        return lst