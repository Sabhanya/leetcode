from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x: int) -> int:
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return low   # first index where nums[mid] >= x

        l = search(target)
        h = search(target + 1) - 1

        if l <= h and l < len(nums) and nums[l] == target:
            return [l, h]
        else:
            return [-1, -1]
