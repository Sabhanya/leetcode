from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        def first_digit(x: int) -> int:
            while x >= 10:
                x //= 10
            return x

        def last_digit(x: int) -> int:
            return x % 10

        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if gcd(first_digit(nums[i]), last_digit(nums[j])) == 1:
                    count += 1
        return count
