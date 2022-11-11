class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d=len(list(set(nums)))
        k=list(set(nums))
        k.sort()
        for i in range(0,len(k)):
            nums[i]=k[i]
    
        return d