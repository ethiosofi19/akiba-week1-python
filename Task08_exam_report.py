stu_name = input("What's your name? ")

py = int(input("your Python score? "))
eng = int(input("your English score? "))
math = int(input("your Mathematics score? "))

ave = (py+eng+math)/3

print("========================================\n\tSTUDENT RESULT\n========================================\n")
print("Student: ", stu_name)
print("\nPython:\t",py)
print("English:\t",eng)
print("Mathematics:\t",math)
print("----------------------------------------")
print("Average:\t",ave)
print("========================================")

