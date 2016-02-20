from stack import Stack

def par_checker(symbol_string):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				s.pop()

		index = index + 1

	if s.is_empty() and balanced:
		return True
	else:
		return False


