class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[0]*len(strs)
        d={}
        for i in range(len(strs)):
            l[i]=''.join(sorted(strs[i]))
        for i in range(len(l)):
            if l[i] in d:
                d[l[i]]=d[l[i]]+[strs[i]]
            else:
                d[l[i]]=[strs[i]]
            
            
        return (list(d.values()))
        
