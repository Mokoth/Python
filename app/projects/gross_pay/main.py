# Gross Pay Project

# Write a program to prompt the user for hours and rate per hour to compute gross pay. 
# You need to take into account that the result has exactly two digits after the decimal place.

hours = float(input('Enter hours: '))
rate = float(input('Enter company rate: '))

normal_pay = hours * rate
# print(round(gross_pay, 2))


# Gross Pay with Overtime

# Rewrite the Gross Pay Project program to give the employee 1.5 times the hourly rate for hours worked
# above 40 hours. 
# Here again the program prompts the user for hours and rate per hour to compute gross pay. 
# You need to take into account that the result has exactly two digits after the decimal place.

# Hint: overtime = hour - 40
# if hours <= 40:
#     print(normal_pay)
# else:
#     overtime = hours - 40
#     overtime_pay = (overtime * 1.5) * rate
#     gross_pay = (40 * rate) + overtime_pay
#     print(gross_pay)


if hours > 40:
    overtime = hours - 40
    overtime_pay = (overtime * 1.5) * rate
    gross_pay = (40 * rate) + overtime_pay
    print(gross_pay)
else:
    print(normal_pay)