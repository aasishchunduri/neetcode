class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=''
        for i in s:
            if i.isalnum(): 
                l=l+i.lower()
            else:
                continue
        if l==l[::-1]:
            return True
        else:
            return False
    
