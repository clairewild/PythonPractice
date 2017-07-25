# Takes an array of integers and returns true if any three consecutive elements sum to seven
def lucky_sevens(numbers):
	if len(numbers) >= 3:
		i = 0
		while i < len(numbers) - 2:
			sum = numbers[i] + numbers[i + 1] + numbers[i + 2]
			if sum == 7:
				return True
			else:
				i += 1
	return False

# Takes an array of integers and returns sum of all the odd elements
def oddball_sum(numbers):
	sum = 0
	for x in numbers:
		if x % 2 != 0:
			sum += x
	return sum

# Takes a string and returns string with all the vowels removed
def disemvowel(string):
	new_string = ""
	for x in string:
		if x != "a" and x != "e" and x != "i" and x != "o" and x != "u":
			new_string = new_string + x
	return new_string
	
# Tests	
print (lucky_sevens([2,1,5,1,0]) == True)
print (lucky_sevens([0,-2,1,8]) == True)
print (lucky_sevens([7,7,7,7]) == False)
print (lucky_sevens([3,4,3,4]) == False)

print (oddball_sum([1,2,3,4,5]) == 9)
print (oddball_sum([0,6,4,4]) == 0)
print (oddball_sum([1,2,1]) == 2)

print (disemvowel("foobar") == "fbr")
print (disemvowel("ruby") == "rby")
print (disemvowel("aeiou") == "")
