#!/usr/bin/python
import sys
import subprocess
import commands
import getpass
import time
import telnetlib
import os
#from globals import *
from globals1 import varList
#import globals

#global device_name

#buil_name = (sys.argv[1])
#ip = "IP"

def addition(buil_name):
	for ip in varList:
		image = buil_name + '_' + ip
		print image
 	#return image

def ip_address(b):
 	print "Let's talk about %s." % b
 	#return globals.b
 	#return b
 
 
if __name__=="__main__":
	buil_name = (sys.argv[1])
	device_name = (sys.argv[1])
	addition(buil_name)
 	ip_address(device_name)