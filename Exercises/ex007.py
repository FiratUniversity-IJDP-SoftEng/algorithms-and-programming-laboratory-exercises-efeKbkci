# Your Student ID: 230543007
# Your Name and Surname: Efkan Efe Kabakcı

import sys

def getFrequencyReport(word: str) -> dict:
    letters = list(word)
    letters.sort()
    report = dict()

    for letter in letters:
        report[letter] = letters.count(letter)

    return report

word = input("Enter a string: ")
report = getFrequencyReport(word)

with open(".\Exercises\ex007_output.txt", "w") as file:
    sys.stdout = file
    [print(key, value) for key, value in report.items()]