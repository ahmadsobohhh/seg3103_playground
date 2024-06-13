class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Dividing by zero does not work")
        return a / b
        
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
