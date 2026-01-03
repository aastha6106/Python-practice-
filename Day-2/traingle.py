def triangle_type(a: float, b: float, c: float) -> str:
	# Validate positive sides
	if a <= 0 or b <= 0 or c <= 0:
		return 'Invalid: sides must be positive'
	# Triangle inequality
	if not (a + b > c and a + c > b and b + c > a):
		return 'Invalid: not a triangle'
	# Determine type
	if a == b == c:
		return 'Equilateral'
	if a == b or b == c or a == c:
		return 'Isosceles'
	return 'Scalene'


if __name__ == '__main__':
	try:
		side1 = float(input('Enter length of first side: ').strip())
		side2 = float(input('Enter length of second side: ').strip())
		side3 = float(input('Enter length of third side: ').strip())
	except Exception:
		print('Please enter valid numeric side lengths.')
	else:
		print(triangle_type(side1, side2, side3))