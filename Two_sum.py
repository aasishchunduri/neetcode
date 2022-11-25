class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        h=len(numbers)-1
        while True:
            if numbers[l]+numbers[h]>target:
                h=h-1
            elif numbers[l]+numbers[h]<target:
                l=l+1
            elif numbers[l]+numbers[h]==target:
                return l+1,h+1
                break



