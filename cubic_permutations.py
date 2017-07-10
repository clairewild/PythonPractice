# Finds all the permutations of a string
def permutations(string):
	if len(string) <= 1:
		yield string
	else:
		for i in range(len(string)):
			for p in permutations(string[:i] + string[i+1:]):
				yield string[i] + p


# Checks to see if an integer is a perfect cube
def is_cube(num):
	x = num ** (1/3)
	x = round(x)
	if x ** 3 == num:
		return True
	else:
		return False


# Finds the smallest cube, x, greater than min for which n perputations of digits are also cubes
def cubic_permutations(n, min):
	x = min + 1
	cubes = 0
	for p in permutations(str(x)):
		if is_cube(int(p)):
			cubes += 1
			if cubes == n:
				return x
		x += 1
