#  Employee Payslip

name = input("What is your name? ")
salary = int(input("What is your basic salary? "))
trans = int(input("Transport allowance? "))
food = int(input("Food allowance? "))

gross_salary = salary + trans + food


print("========================================")
print("\tEMPLOYEE PAYSLIP")
print("========================================")
print("\nEmployee: ", name)
print("\nBasic Salary:\t", salary, "ETB")
print("Transport Allowance:\t",trans,"ETB")
print("Food Allowance:\t", food,"ETB")
print("----------------------------------------")
print("Gross Salary:\t",gross_salary,"ETB")
print("========================================")

