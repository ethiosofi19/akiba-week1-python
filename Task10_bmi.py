name = input("What's your name dear customer? ")
weight = int(input("Weight in kilograms? "))
height = float(input("Height in meters? "))

bmi = weight/(height*height)

print("========================================\n\tBMI REPORT\n========================================\n")
print("Name: ", name)
print("Weight: ", weight," kg")
print("Height: ", height, "m\n")
print("BMI: ", bmi)
print("========================================")

