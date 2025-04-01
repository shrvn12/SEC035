def largest():
    try:
        max = None
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        c = int(input('Enter third number: '))

        if a >= b and a >= c:
            max = a
        elif b >= a and b >= c:
            max = b
        else:
            max = c
        print("\n📌 The largest number is: ", max)
    except:
        print('Invalid input. Please enter a valid number. 🙄')
        exit = input('Exit? y/N: ')
        if exit == "y" or exit == "Y":
            return
        print('\n')
        largest()

largest()
print()

def Starpyramid():
    rows = 7
    for i in range(rows):
        print(" "*(rows-i)+"* "*i)

Starpyramid()

