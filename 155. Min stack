class MinStack:
    def __init__(self):
        self.tos=-1
        self.stack=[]
    def push(self, x: int) -> None:
        self.tos+=1
        self.stack.append(x)
    def pop(self) -> None:
        if self.tos==-1:
            return 0
        else:
            del self.stack[-1]
            self.tos-=1
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return min(self.stack)
