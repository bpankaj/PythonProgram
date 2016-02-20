with open('fileContent.py', 'r+') as infile:
	for line in infile.readLines():
    	if "def" in line:
    		infile.write('\n'.join('added word')
      		#infile.write('\n'.join(line[i:i+50] for i in xrange(0,len(line), 50)))
      		#infile.write('\n'.join('added word')
http://stackoverflow.com/questions/18410111/python-insert-new-line-if-line-has-more-than-50-characters
      		