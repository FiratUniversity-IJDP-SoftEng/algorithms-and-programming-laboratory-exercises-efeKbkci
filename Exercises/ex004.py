# Your Student ID: 230543007
# Your Name and Surname: Efkan Efe Kabakcı

def calculateArea(r: int) -> float:
    PI = 3.14
    return (r ** 2) * PI 

radius = float(input("Input the radius of the circle: "))

print(f"The area of the circle with radius {radius} is: {calculateArea(radius):.2f}")