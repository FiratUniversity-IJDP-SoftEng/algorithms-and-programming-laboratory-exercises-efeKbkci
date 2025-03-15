# Your Student ID: 230543007
# Your Name and Surname: Efkan Efe Kabakcı

import sys

outputFile = open("ex006_output.txt", "w")
sys.stdout = outputFile

l = list(range(11))
print("Original List: ", l)

l.reverse()
print("Reversed List: ", l)

l.reverse() # return it to its original state
[l.append(number) for number in range(11,14)]
print("Changed List: ", l)

print("List Lenght: ", l.__len__())

[l.pop(number) for number in [0,-1]]
print("Narrowed List: ", l)

evenList = [number for number in l if number % 2 == 0]
print("Even List: ", evenList)

outputFile.close()