def prime1(low, high):
	for num in range(low, high + 1):
	# prime numbers are greater than 1
		if num > 1:
			for i in range(2,num):
				if (num % i) == 0:
					break
			else:
				print(num)