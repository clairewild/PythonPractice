def sum_of_square(num):
	x = 1
	result = 0
	while x <= num:
		result += x ** 2
		x += 1
	return result


def square_of_sum(num):
	y = 1
	result = 0
	while y <= num:
		result += y
		y += 1
	return result ** 2


def sum_square_diff(z):
	return square_of_sum(z) - sum_of_square(z)