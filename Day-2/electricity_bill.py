def calculate_bill(units: int) -> int:
    if units <= 100:
        return units * 2
    if units <= 200:
        return 100 * 2 + (units - 100) * 3
    return 100 * 2 + 100 * 3 + (units - 200) * 5


if __name__ == '__main__':
    try:
        units = int(input('Enter units consumed: ').strip())
        if units < 0:
            raise ValueError('Negative units')
    except Exception:
        print('Please enter a valid non-negative integer for units.')
    else:
        total = calculate_bill(units)
        print(f'Total electricity bill for {units} units: ₹{total}')

