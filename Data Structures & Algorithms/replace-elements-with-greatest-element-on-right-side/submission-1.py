class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # iterating over index:
        for i in range(len(arr)):
            # replace last element with -1
            if i == len(arr) - 1:
                arr[i] = -1
            else:   # if it's not the last element:
                # replace current element with max(current, rest)
                arr[i] = max(arr[i + 1:])
        return arr