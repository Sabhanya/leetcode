from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = dict()
        for i in range(3):
            d[i] = 0

        # Count occurrences
        for num in nums:
            d[num] = d[num] + 1

        # Clear list before rebuilding
        nums.clear()

        # Fill back sorted values
        for k, v in d.items():
            for i in range(v):
                nums.append(k)

