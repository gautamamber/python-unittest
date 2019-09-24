class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return False
    
c = Calculator(3,4)
print(c.add())
print(c.subtract())