from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def isSelfDividing(n: int) -> bool:
            for d in str(n):
                if d == "0" or n % int(d) != 0:
                    return False
            return True
        
        res = []
        for i in range(left, right + 1):
            if isSelfDividing(i):
                res.append(i)
        return res

