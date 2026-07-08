class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min1=min(nums)
        max1=max(nums)
        return gcd(min1,max1)     
