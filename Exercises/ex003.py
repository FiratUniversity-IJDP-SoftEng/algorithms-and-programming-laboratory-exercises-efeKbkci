# Your Student ID: 230543007
# Your Name and Surname: Efkan Efe Kabakcı

from datetime import datetime

now = datetime.now()

current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")
current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

print("Current date:", current_date)
print("Current time:", current_time)
print("Current date and time:", current_datetime)