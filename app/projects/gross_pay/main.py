# Gross Pay Project

# Write a program to prompt the user for hours and rate per hour to compute gross pay. 
# You need to take into account that the result has exactly two digits after the decimal place.

hours = input('Enter hours: ')
rate = input('Enter company rate: ')

gross_pay = float(hours) * float(rate)
print(round(gross_pay, 2))