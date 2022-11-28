# Tip Calculator - My Version#

print('Welcome to the tip calculator.')

Bill = float(input('What was the total bill? '))
Tip = float(input('What percentage tip would you like to give? (10, 12, 15): '))
Tip_prec = Tip/100+1
Total = float(format(Bill * Tip_prec,".2f"))
Split = int(input('How many people to split the bill? '))
Final = format(Total/Split,".2f")

print(f"Each person should pay {Final}")