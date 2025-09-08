class Solution:
    def triangleType(self, nums: list[int]) -> str:
        a, b, c = nums
        
        # Check triangle inequality
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
        
        # Classify
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
