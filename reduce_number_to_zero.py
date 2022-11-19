class Solution:
    def helper(self,n,count):
        if n==0:
            return count
        if n%2==0:
            n=n//2
            count+=1
        else:
            n=n-1
            count+=1
        return self.helper(n,count)
        
        
    def numberOfSteps(self, num: int) -> int:
        count=0
        d=self.helper(num,count)
        return d


