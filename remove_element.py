class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans=0
        k=0
        while k<len(nums):
            if nums[k]!=val:
                k+=1
            else:
                nums.remove(nums[k])