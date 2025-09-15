from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        insert_pos = 0
        
        # Move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        # Fill the rest with zeros
        while insert_pos < n:
            nums[insert_pos] = 0
            insert_pos += 1
            
