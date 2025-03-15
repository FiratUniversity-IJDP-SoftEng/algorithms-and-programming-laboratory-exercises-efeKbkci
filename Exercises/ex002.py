# Your Student ID: 230543007
# Your Name and Surname: Efkan Efe Kabakcı
import sys
import re

version = re.search(r"3\.\d*\.\d*", sys.version)

print(f"Python Version: {version.group()}")

print(f"Version Info: {sys.version_info}")