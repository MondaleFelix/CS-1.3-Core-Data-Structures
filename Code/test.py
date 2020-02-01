
# Converts digit to base 2
def convert_to_decimal(binary):
	digits = [int(i) for i in str(binary)]
	digits.reverse()

	value = 0
	exponent = 0
	for i in digits:
		value += i * exponent
		if exponent == 0:
			exponent = 1
		else:
			exponent *= 2
	return value

print(convert_to_decimal(11010))


def convert_to_binary(decimal):
	binary_number = []
	while decimal is not 0:
		binary_number.append(decimal%2)
		decimal = decimal // 2 


	binary_number.reverse()
	print(binary_number)

# convert_to_binary(150)