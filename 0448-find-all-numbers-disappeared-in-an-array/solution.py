class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark seen numbers by negating the value at their corresponding index
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        # Collect indices with positive numbers -> missing values
        return [i + 1 for i, val in enumerate(nums) if val > 0]
