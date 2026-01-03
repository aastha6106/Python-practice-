num = int(input("Enter the number you want to check: "))
if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is divisible by both 3 and 7.")
else:
    print(f"{num} is not divisible by botth 3 and 7.")