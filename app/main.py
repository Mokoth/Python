# print()
# EOL 

# VALUE AND TYPES
    # strings - > each letter (binary value)
    # integer
    # float
    # boolean True/False

    # type() -> check value type

# VARIABLES
    # assignment (=)
spam = 10
message = 'get back home'
PI = 3.142144
    # variable assignment
spam = 'hello'

# OPERATORS
    # + / - % // **
print(50 / 2) # dividing always retuns float output



# INPUT
name = input('Enter name: ')
# \n -> NEWLINE


# user_name = input('What is your name?\n')
# print(user_name)


years = input('Enter number of years ')
no_weeks = int(years) * 52

print('There are ' + str(no_weeks) +  ' weeks in ' + str(years) + ' years')

# f-string
# print(f"There are {no_weeks} weeks in {years} years")

# Round
print(10 / 3) # 3.3333333333333335
print(int(10 / 3)) # 3
print(round(10 / 3, 2)) # 3.33