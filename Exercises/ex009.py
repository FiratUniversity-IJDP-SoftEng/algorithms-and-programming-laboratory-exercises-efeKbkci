# Your Student ID: 230543007
# Your Name and Surname: Efkan Efe Kabakcı

class Temperature:
    CtoF = "1"
    FtoC = "2"

    @staticmethod
    def celsiusToFahrenheit(C: float) -> float:
        return (C * 9/5) + 32
    
    @staticmethod
    def fahrenheitToCelsius(F: float) -> float:
        return (F - 32) * 5/9
    
if __name__ == "__main__":

    print("Press 1 to convert celsius to fahrenheit")
    print("Press 2 to convert fahrenheit to celsius\n")

    operation = input("Operation: ")

    outputs = {Temperature.CtoF: "Temperature in Celsius: ", Temperature.FtoC: "Temperature in Fahrenheit: "}

    temp = float(input(outputs[operation]))

    convertedTemp = None
    if operation == Temperature.CtoF:
        print(f"Temperature in Fahrenheit -> {Temperature.celsiusToFahrenheit(temp):.2f} F")
    elif operation == Temperature.FtoC:
        print(f"Temperature in Celsius -> {Temperature.fahrenheitToCelsius(temp):.2f} C")