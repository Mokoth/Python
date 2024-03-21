# while True:
#     try:
#         x = int(input("Enter a num: "))
#         break
#     except:
#         print(f'x is not an integer')
#     else:
#         print(f'x is {x}')
# print('Done') 

print("Welcome to Mortgage Calculator: ")
try:
    salary = int(input('Enter salary: '))
    rate = 0
except ValueError:
    print(f'Error: The amount is not an integer')
else:
    if salary >= 2000:
        print(f'Eligible for a mortgage')
        try:
            credit_score = int(input('Enter credit score: '))
        except ValueError:
            print('Error: Credit score')
        else:
            if credit_score > 800:
                rate = 4
                print(f'Your score is {rate}%')
            elif credit_score > 750:
                rate = 6
                print(f'Your score is {rate}%')
            else:
                rate = 8
                print(f'Your score is {rate}%')
            try:
                disability = input("Are you disabled? Y or N: ")
            except ValueError:
                print('Please select either Y or N')
            else:
                if disability == 'Y':
                    rate -= 2
                    print(f'Final rate is {rate}')
    else:
        print('Not eligible')
finally:
    print(f'Thanks for using the calculator!')



# Consider -ve numbers
# Consider both upper and lower
# looping incase of an error input by user