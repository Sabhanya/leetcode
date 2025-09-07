class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2   # sum of 0...n
        return total - sum(nums)
        
