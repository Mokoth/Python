while True:
    try:
        x = int(input("Enter a num: "))
        break
    except:
        print(f'x is not an integer')
    else:
        print(f'x is {x}')
print('Done')