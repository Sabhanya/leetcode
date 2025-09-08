class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def isSelfDividing(num: int) -> bool:
            temp = num
            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    return False
                temp //= 10
            return True

        result = []
        for n in range(left, right + 1):
            if isSelfDividing(n):
                result.append(n)
        return result
        
