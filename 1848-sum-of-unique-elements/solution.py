class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans=0
        count=Counter(nums)
        for (key,val) in count.items():

            if val==1:
                ans+=key
        return ans
        
