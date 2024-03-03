# Trip Cost Calculator Project

# Write a program which calculates trip cost for a user.

# Create a greeting for your program.
# Ask the user for number of days.
# Ask the user for hotel price.
# Ask the user for flight price.
# Ask the user for rental car price.
# Ask for other expenses.
# Combine all expenses together and print with 2 digits after decimal places.

print('Welcome to the Trip Cost Calculator!')
days = input('How many days will you stay? ')
hotel_cost_per_night = input('How much does hotel cost per night? $ ')
flight_cost = input('How much does flight cost? $ ')
rental = input('If you need rental car please enter the price otherwise enter zero. $10 ')
other_expenses = input('Enter other possible expenses $ ')

hotel_expenses = int(days) * float(hotel_cost_per_night)

total_expenses = round((hotel_expenses + int(flight_cost) + int(rental) + int(other_expenses)), 2)

print(f"Total cost: ${total_expenses}")
