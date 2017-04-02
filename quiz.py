# Returns the sum of each number multiplied by it's postion in the array
def crazy_sum(numbers):
	sum = 0
	i = 0
	for x in numbers:
		sum = sum + (x * i)
		i += 1
	return sum

# Returns the number of perfect squares less than max
def square_nums(max):
	squares = 0
	base = 1
	while base ** 2 < max:
		squares += 1
		base += 1
	return squares

# Returns an array of integers divisible by either three or five but not both, that are less than max
def crazy_nums(max):
	result = []
	x = 3
	while x < max:
		if x % 3 == 0:
			three = True
		else:
			three = False

		if x % 5 == 0:
			five = True	
		else:
			five = False	

		if three != five:
			result.append(x)
			x += 1
		else:
			x += 1
			
	return result