# Your Student ID: 230543007
# Your Name and Surname: Efkan Efe Kabakcı
import re

sampleText = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
exceptedText = ""

pattern = re.compile(r"[,!\.]")
splittedTextList = re.split(pattern, sampleText)

exceptedText = f"""
{",".join(splittedTextList[:3])}
    {splittedTextList[3].strip()}!
        {splittedTextList[4].strip()},
        {splittedTextList[5].strip()}.
{",".join(splittedTextList[6:9])}
    {splittedTextList[-1].strip()}
"""

print(exceptedText)