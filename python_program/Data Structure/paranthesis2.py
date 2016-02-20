#from stack import Stack

def par_checker(symbol_string):
	s = []
	balanced = True
	index = 0
	while index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		if symbol in "({[":
			s.append(symbol)
		else:
			if s == []:
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False

		index = index + 1

	if s == [] and balanced:
		return True
	else:
		return False

def matches(open, close):
	opens = "({["
	closes = ")}]"
	return opens.index(open) == closes.index(close)


