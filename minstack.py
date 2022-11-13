class MinStack:

    def __init__(self):
        self.a=[]
        self.min=99999
        

    def push(self, val: int) -> None:
        self.a.append(val)
        if val<self.min:
            min=val


        
    def pop(self) -> None:
        self.a.pop(len(self.a)-1)
        if  
        

    def top(self) -> int:
        return self.a[len(self.a)-1]
        

    def getMin(self) -> int:
        return min(self.a)