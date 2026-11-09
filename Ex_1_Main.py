from Ex_1_Data import load_initial
from Ex_1_Processing import total_salary
from colorama import Fore
path = "Initial_data.txt"
lines = load_initial(path)
total, average_salary = total_salary(lines)
print (Fore.GREEN + f'Загальна сума заробітної плати: {Fore.RED}{total}, {Fore.GREEN}Середня заробітна плата: {Fore.RED}{average_salary}')