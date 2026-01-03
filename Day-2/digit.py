num = int(input("Enter a number: "))
num = abs(num)  # Handle negative numbers by taking absolute value

if num < 10:
    print(f"{num} is a 1 digit number")
elif num < 100:
    print(f"{num} is a 2 digit number")
elif num < 1000:
    print(f"{num} is a 3 digit number")
else:
    print(f"{num} has more than 3 digits")
