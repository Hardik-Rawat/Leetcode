class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span= 1
        while self.stack and self.stack[-1][0] <= price:
            prevVal, prevspan = self.stack.pop()
            span += prevspan
        
        self.stack.append((price, span))
        return span