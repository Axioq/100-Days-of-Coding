# BMI Calculator w/ F String#

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

w=float(weight)
h=float(height)

bmi=round(w/(h**2),2)

print(f"Your BMI is {bmi}")