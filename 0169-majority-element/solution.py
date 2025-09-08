from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        t = n // 2
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for k, v in freq.items():
            if v > t:   # strictly greater than floor(n/2)
                return k
