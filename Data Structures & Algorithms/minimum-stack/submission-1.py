class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minValue = val
        else:
            self.stack.append(val - self.minValue)
            if val < self.minValue:
                self.minValue = val        

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop <= 0:
            self.minValue = self.minValue - pop
        

    def top(self) -> int:
        top = self.stack[-1]
        if top <= 0:
            return self.minValue
        else:
            return top + self.minValue


    def getMin(self) -> int:
        return self.minValue
        
