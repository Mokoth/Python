# Celsius to Fahrenheit Project

# Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the converted temperature. 
# Formula : (°C × 9/5) + 32 = °F

print('Celsius to Fahrenheit conversion.')

celsius = input('Enter Temperature in Celsius: ')

fahrenheit = (float(celsius) * 9/5) + 32

# print(fahrenheit)
print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")