a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
res = a + b
print(f"The sum is: {res}")



num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")



num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")



word = input("Enter a word: ")
if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")


num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(f"Largest number is: {max(numbers)}")


string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"Reversed string: {reversed_string}")


num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


num = int(input("Enter a number: "))
total = sum(int(digit) for digit in str(num))
print(f"Sum of the digits: {total}")


num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
