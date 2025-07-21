class Solution:
    def isFascinating(self, n: int) -> bool:
        S=str(n)+str(n*2)+str(n*3)
        return ''.join(sorted(S))=="123456789"
        
