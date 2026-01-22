
numbers = [1, 2, 3]

print(f"Original list: {numbers}")
print(f"Length: {len(numbers)}")


numbers.extend([4, 5, 6])

print(f"After extend: {numbers}")
print(f"Length: {len(numbers)}")


additional = [7, 8, 9, 10]
numbers.extend(additional)

print(f"Final list: {numbers}")
print(f"Length: {len(numbers)}")

numbers.extend(range(11, 14))

print(f"After range extend: {numbers}")
print(f"Length: {len(numbers)}")
