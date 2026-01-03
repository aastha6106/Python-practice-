try:
    num = float(input("Enter the number: "))
except Exception:
    print("Please enter a valid number.")
else:
    if 10 <= num <= 50:
        print(f"{num} lies between 10 and 50")
    else:
        print(f"{num} does not lie between 10 and 50")