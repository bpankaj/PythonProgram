import os
#import sys

def addLoggerInTheFile(file_name):
	"""
	Add logger into the classes, functions, functions inside class and inner functions
	"""
	fObj = open(file_name, 'r+')
	lines = fObj.readlines()
	fObj.close()
	fwObj =  open('other_file.py', 'w')
	class_name = ''
	function_name = ''
	log_statement = "LOG.info(_LI(\"soumiyajit::  " + file_name
	for k in lines:
		if k.startswith("class"):
			class_name = k.split()[1].split('(')[0]
			log = log_statement + "/Class " + class_name + " \"))\n"
			w = k + "    " + log
			fwObj.write(w)
		elif k.startswith('    def'):
			function_name = k.split(' ')[5].split('(')[0]
			log = log_statement + "/Class " + class_name + "/ " + function_name + " \"))\n"
			w = k + "        " + log
			fwObj.write(w)
		elif k.startswith('        def'):
			function_name = k.split()[1].split('(')[0]
			log = log_statement + '/Class ' + class_name + "/ " + function_name + " \"))\n"
			w = k + "            " + log
			fwObj.write(w)
		elif k.startswith('def'):
			function_name = k.split()[1].split('(')[0]
			log = log_statement + '/ ' + function_name + " \"))\n"
			w = k + "    " + log
			fwObj.write(w)
		else:
			fwObj.write(k)
	fwObj.close()

	fObj1 = open(file_name, 'r+')
	fObj1.seek(0)
	fObj1.truncate()
	fObj2 = open('other_file.py', 'r')
	buffer1 = fObj2.read()
	log_import = """#soumiyajit
	from oslo_log import log as logging
	from heat.common.i18n import _LE
	from heat.common.i18n import _LI
	LOG = logging.getLogger(__name__)"""
	fObj1.write(log_import)
	fObj1.write(buffer1)
	fObj1.close()
	fObj2.close()

rootdir = "/home/pankaj/python_program/logs/cfn"
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filename = os.path.join(subdir, file)
        if filename.endswith(".py"):
        	addLoggerInTheFile(filename)


#def getFileFromRootDir(rootDir):
#	"""
#	Get file from different directory
#	"""
#	for subdir, dirs, files in os.walk(rootDir):
#		for file in files:
#			filename = os.path.join(subdir, file)
#	       	if filename.endswith(".py"):
#        		addLoggerInTheFile(filename)


#if __name__ == '__main__':
#	getFileFromRootDir(sys.argv[1])
