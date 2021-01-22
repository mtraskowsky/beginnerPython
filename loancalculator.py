# Name: Maria Traskowsky
# Section: (C) TU 11:00am - 12:15pm
# Description: This program is a loan calculator that calculates how much money the user
# will repay over the life of the loan. 
# The program takes user inputs for the amount borrowed, the years required to pay off
# the loan, and the interest rate. The program then calculates and displays required
# annual payments, monthly payments, and what the total amount paid will be for the 
# life of the loan.
# The program asks for the user to input annual salary, and calculates whether they
# should refinance, seek financial counseling, or whether they are on track to pay 
# off the loan.


# ask for user input for amount of money borrowed
amount_borrowed = float(input("How much money did you borrow? "))

# ask for user input for number of years required to pay back loan in full
years_to_pay_off = float(input("\nHow many years will it take you to pay off the loan? "))

# ask for user input for interest rate of the loan
interest_rate = str(input("\nWhat is the interest rate (in decimal form) on your loan? "))

# calculate annual payment using user inputs
annual_payment = (((1 + float(interest_rate)) ** years_to_pay_off) * amount_borrowed * float(interest_rate)) / (((1 + float(interest_rate)) ** years_to_pay_off) - 1)

# print annual payment
print ("\nYour annual payment is: ")
print('${:,.2f}'.format(annual_payment))

#calculate and print monthly payment
monthly_payment = (annual_payment / 12)
print ("\nYour monthly payment is: ")
print('${:,.2f}'.format(monthly_payment))

# calculate and print total amount paid for life of the loan
total_amount_paid = annual_payment * years_to_pay_off
print("\nThe total amount paid for the life of the loan is: ")
print('${:,.2f}'.format(total_amount_paid))

# ask for user input for annual salary
annual_salary = float(input("\nWhat is your annual salary? "))

# calculate monthly income
monthly_income = annual_salary / 12

# if the monthly payment is larger than monthly income and the interest rate is more than 5%
if monthly_payment > monthly_income and interest_rate > .05:
    print("\nYou should refinance.")
# otherwise, if monthly payment is more than monthly income but interest rate is not more than 5%
elif monthly_payment > monthly_income:
    print("\nYou should seek financial counseling.")
# otherwise, if monthly payment is less than monthly income
else:
    print("\nIf you make all of the payments, you should get your loan paid off in time.")
        