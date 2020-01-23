income = float(input("How much do you earn each month? "))
principal = float(input("How much loan do you need? "))
time = int(input("How many month(s) will it take to repay the loan? "))
rate = 3

annual_interest = (principal * rate * time) / 100
monthly_interest = annual_interest / 12

if income < principal / 20:
    print("Sorry, you don't qualify for the loan")
elif income >= principal / 20:
     print(f"You qualify for the loan of {principal} cedis at {monthly_interest} cedis interest at the end of {time} month(s)")