from math import inf

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        current_min = x
        if self.stack:
            current_min = min(x, self.stack[-1][1])
        self.stack.append((x, current_min))

    def pop(self):
        return self.stack.pop()[0]

    def getMin(self):
        return self.stack[-1][1]

    def top(self):
        return self.stack[-1][0]