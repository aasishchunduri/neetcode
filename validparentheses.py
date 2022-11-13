class Solution:
    def isValid(self, s: str) -> bool:
        l=list(s)
        d=["(","{","["]
        d1=[")","}","]"]
        a=[]
        for i in range(len(l)):
            if l[i] in d:
                a.append(l[i])
            else:
                ind=d1.index(l[i])
                if len(a)>0 and d[ind]==a[len(a)-1]:
                    a.pop()
                else:
                    return False
                
                    break
        if len(l)!=0 and len(a)==0:
            return True
        else:
            return False