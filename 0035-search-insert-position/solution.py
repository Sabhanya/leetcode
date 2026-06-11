from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # low, high = 0, len(nums) - 1

        # while low <= high:
        #     mid = (low + high) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         low = mid + 1
        #     else:
        #         high = mid - 1

        # return low   # insertion point
        l=0
        r=len(nums)-1
        if target>nums[r]:
            return r+1
        if target<nums[l]:
            return l
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        if nums[m]<target:
            return m+1
        else:
            return m
    
