print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $"))
percentageTip = int(input("What percentage tip would you like to give? 10, 12, 15, 20? "))
percentage = percentageTip/100
split = int(input("How many people to split the bill? "))
payPerPerson = (totalBill * (1 + percentage)/split)
print(f"Each person should pay: {payPerPerson:.2f}")