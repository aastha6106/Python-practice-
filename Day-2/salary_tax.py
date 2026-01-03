salary = float(input("Enter your salary: "))
if salary <= 250000:
    tax = salary * 0
elif salary <= 500000:
    tax = salary * 0.05
elif salary <= 1000000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

print(f"Salary: ₹{salary}")
print(f"Tax: ₹{tax}")
print(f"Net Salary: ₹{salary - tax}")










