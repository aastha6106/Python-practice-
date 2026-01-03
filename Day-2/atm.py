balance = int(input("Enter your account balance: "))
withdraw_amount = int(input("Enter the amount to withdraw: "))
if withdraw_amount <= balance:
    balance -= withdraw_amount
    print(f"withdrawal successful. New balance is {balance}.")
else:
    print("Insuffiecient balance. Withdrawal failed.")