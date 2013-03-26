#! /usr/bin/env python

import sys
import os
import re
import math


argv = len(sys.argv)
if argv != 2:
	print "usage: assemblyCheck.py <filename>"
	sys.exit(1)


argo = sys.argv[1]

if (os.access(argo, os.R_OK) == 0):
	print argo, "is not readable"
	sys.exit(2)
	
InFile = open(argo, "r")

	
name = r"((lw)|(sw)|(add)|(sub)|(mul)|(div)|(beq)|(jmp))\s"
numbercheck = r"(\$t[0-7])|(!(([0-9][0-9]?[0-9]?)|(10[0-1][0-9])|(102[0-4])))$"

for assembly in InFile:
	
	valid = re.match(name, assembly)
	recordline = assembly
	assembly = assembly.split(" ")
	assembly = assembly[1]
	assembly = assembly.split(",")
	for line in assembly:
		temp = re.match(numbercheck, line)
		if valid != 0:
			valid = temp
			
	
	if not (valid):
		print "Error: invalid line %s" %(recordline,),