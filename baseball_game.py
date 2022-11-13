class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in range(len(operations)):
            if operations[i]=="C":
                l.pop(len(l)-1)
                print(l)
            elif operations[i]=="D":
                l.append(int(l[len(l)-1])*2)
                print(l)
            elif operations[i]=="+":
                l.append(int(l[len(l)-1])+int(l[len(l)-2]))
            else:
                l.append(int(operations[i]))
                print(l)
        return sum(l)