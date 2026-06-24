from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [0] * n
        # left, right = 0, n - 1
        # pos = n - 1   # fill from the back

        # while left <= right:
        #     if abs(nums[left]) > abs(nums[right]):
        #         res[pos] = nums[left] * nums[left]
        #         left += 1
        #     else:
        #         res[pos] = nums[right] * nums[right]
        #         right -= 1
        #     pos -= 1

        # return res
        result=[num**2 for num in nums ]
        result.sort()
        return result
