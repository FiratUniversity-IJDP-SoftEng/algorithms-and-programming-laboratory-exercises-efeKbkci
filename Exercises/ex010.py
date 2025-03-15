# Your Student ID: 230543007
# Your Name and Surname: Efkan Efe Kabakcı

class Calculator:

    @staticmethod
    def add(v1:float, v2:float) -> float:
        return v1 + v2
    
    @staticmethod
    def subtract(v1:float, v2:float) -> float:
        return v1 - v2
    
    @staticmethod
    def multiply(v1:float, v2:float) -> float:
        return v1 * v2 
    
    @staticmethod
    def divide(v1:float, v2:float) -> float:
        if not v2:
            return None
        return v1 / v2 
    
    @staticmethod
    def getOperation(code: int) -> dict:
        operationDict = {"1": Calculator.add, "2": Calculator.subtract, "3": Calculator.multiply, "4": Calculator.divide}
        return operationDict[code]

print("Addition: 1 | Subtraction: 2 | Multiplication: 3 | Division: 4\n")

operationCode = input("Operation: ")
operation = Calculator.getOperation(operationCode)

v1, v2 = [int(input(f"Number {i}: ")) for i in [1,2]]
print("Result:", operation(v1, v2))