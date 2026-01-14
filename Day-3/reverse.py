num = int(input("Enter a number of your choice: "))
reversed_num = 0

n = abs(num)
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n = n // 10

if num < 0:
    reversed_num = -reversed_num
print(f"The reversed number is: {reversed_num}")
