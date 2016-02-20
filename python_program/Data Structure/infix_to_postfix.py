def infix_to_postfix(infix_expr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	op_stack = []
	postfix_list = []
	token_list = infix_expr.split()

	for token in token_list:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfix_list.append(token)
		elif token == "(":
			op_stack.append(token)
		elif token == ")":
			top_token = op_stack.pop()
