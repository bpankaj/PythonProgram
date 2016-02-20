UNITS = ['KB', 'MB', 'GB', 'TB', 'PB']

def sizeInByte(sz):
	if sz < 0:
		raise ValueError('number < 0')

	factor = 1024
	for i in range(len(UNITS)):
		if sz < factor:
			if i == 0:
				return '{0:.1f} {1[0]}'.format(sz, UNITS)
			elif i == 1:
				return '{0:.1f} {1[1]}'.format(sz, UNITS)
			elif i == 2:
				return '{0:.1f} {1[2]}'.format(sz, UNITS)
			elif i == 3:
				return '{0:.1f} {1[3]}'.format(sz, UNITS)
			else:
				return '{0:.1f} {1[4]}'.format(sz, UNITS)
		else:
			sz /= factor

	raise ValueError('Too big')