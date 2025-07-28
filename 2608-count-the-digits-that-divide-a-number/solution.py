class Solution:
    def countDigits(self, num: int) -> int:
        a = str(num)
        count = 0
        for i in a:
            digit = int(i)
            if digit != 0 and num % digit == 0:
                count += 1
        return count        
