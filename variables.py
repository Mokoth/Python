# method of storing data for reuse
just_a_variable = 'I am a variable'
print(just_a_variable)

# variable update
just_a_variable = 'I am an updated variable'
print(just_a_variable)

# Receipts for Lovely Loveseats - project

# Storing the names and prices of a furniture store’s catalog in variables, then process the total price and item list of customers, printing them to the output

# Add first item and price
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'

lovely_loveseat_price = 254.00

# Add second item and price
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'

stylish_settee_price = 180.50

# Add third item and price
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'

luxurious_lamp_price = 52.15

# Calculating sales tax
sales_tax = .088

# Customer one total
customer_one_total = 0

# Customer one item description
customer_one_itemization = ''

# Purchase lovely_loveseat and new price
customer_one_total += lovely_loveseat_price

# Updated item description after purchase
customer_one_itemization += lovely_loveseat_description

# Updated price - Purchase of Luxurious Lamp
customer_one_total += luxurious_lamp_price

# Updated item - description after purchase
customer_one_itemization += luxurious_lamp_description

# Checkout - calculating sales tax
customer_one_tax = customer_one_total * sales_tax

# Adding sales tax to customers' total
customer_one_total += customer_one_tax

# print receipts
print('Customer One Items:')
print(customer_one_itemization)
print('Customer One Total:')
print(customer_one_total)


myint = 5
myfloat = 12.43

mystr = 'This is a string'

mybool = True

mylist = [0, 1, 'two', 3.2, False]

# print(mylist[2])

# Slice
# print(mylist[1:3])

# step
# print(mylist[1:5:2])

# reverse
# print(mylist[::1])

mytuple = (0, 1, 2)

mydict = {'one': 1, 'two': 2}

# access key:value
# print(mydict['one'])

# ERROR: variables of different types cannot be combined
# print('string type' + 234)
# print('string type' + str(234))


# Global vd Local variables
def somefunc():
    global mystr
    mystr = 'def'
    print(mystr)
somefunc()
print(mystr)

del mystr
print(mystr)

# Global
# Local
# del a variable