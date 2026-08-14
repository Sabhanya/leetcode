class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        r=[]
        for i in range(len(nums)//2):
            minn=min(nums)
            maxx=max(nums)
            av=(minn+maxx)/2
            r.append(av)
            nums.remove(minn)
            nums.remove(maxx)
        return len(list(set(r)))