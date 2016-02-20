def base_convertor(decimal, base):
	digits = "0123456789ABCDEF"
	listStack = []
	while decimal > 0:
		rem = decimal % base
		listStack.append(rem)
		decimal = decimal // base

	new_string = ""
	while listStack:
		new_string = new_string + digits[listStack.pop()]
	return new_string



