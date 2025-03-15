# Your Student ID: 230543007
# Your Name and Surname: Efkan Efe Kabakcı
import sys

def prepareOutput(row: int) -> str:
    asterisksNumber = 2 * row - 1
    spaceNumber = (MAX - asterisksNumber) // 2
    return f"{' ' * spaceNumber}{"*" * asterisksNumber}{' ' * spaceNumber}"

row = int(input("Number of row: "))
MAX = 2 * row - 1

with open(r".\Exercises\ex008_output.txt", "w") as f:
    sys.stdout = f
    print("Number of row: ", row)
    [print(prepareOutput(i)) for i in range(1, row + 1)]


    