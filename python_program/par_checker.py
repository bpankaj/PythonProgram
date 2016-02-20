def par_checker(symbol_string):
	listStack = []
	balanced = True
	index = 0
	while index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		if symbol in "({[":
			listStack.append(symbol)
		else:
			if not listStack:
				balanced = False
			else:
				top = listStack.pop()
				if not matches(top, symbol):
					balanced = False
		index = index + 1

	if balanced and not listStack:
		return True
	else:
		return False

def matches(open, close):
	opens = "({["
	closes = ")}]"
	return opens.index(open) == closes.index(close)



