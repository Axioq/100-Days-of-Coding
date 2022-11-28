# Your Life in Weeks #

age = int(input("What is your current Age?"))

months = int(90*12) - int(age * 12)
weeks = int(90*52) - int(age * 52)
days = int(90*365) - int(age * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left")