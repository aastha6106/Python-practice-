fruits = ["apple", "banana", "orange", "grape", "banana"]
print(f"Original list: {fruits}")
fruits.remove("orange")
print(f"After remove('orange'): {fruits}")
removed = fruits.pop(1)
print(f"After pop(1) - removed '{removed}': {fruits}")
last = fruits.pop()
print(f"After pop() - removed '{last}': {fruits}")
numbers = [10, 20, 30, 40, 50]
print(f"\nNumbers list: {numbers}")
del numbers[2]
print(f"After del numbers[2]: {numbers}")
test_list = [1, 2, 3, 4, 5]
print(f"\nTest list: {test_list}")
test_list.clear()
print(f"After clear(): {test_list}")
