#! /usr/bin/env python

import sys
import os
import math
def convert2binary(num):
	arr = []
	for i in range(32):
		arr.append(0)
	for i in range(32):
		temp = num%2
		num /= 2
		arr[31-i] = temp
	return arr
	



def displayBinary(num):
	out = ""
	arr = convert2binary(num)
	for i in range(16):
		out += str(arr[16+i])
	print out
	
def getBit(index, num):
	arr = convert2binary(num)
	if (index > 31) or (index < 0):
		raise ValueError("OMG!!! That's over 31, not cool bro!")
	return arr[31-index]

def getPartialValue(index1, index2, num):
	arr = convert2binary(num)
	out = []
	if index1 < index2:
		ihigh = index2
		ilow = index1
	else:
		ihigh = index1
		ilow = index2
	while ihigh >= ilow:
		out.append(getBit(ihigh, num))
		ihigh -= 1
	count = 1
	final = 0
	for I in range(len(out)):
		final += pow(2,I)*out[len(out)-1-I]
	return final



#displayBinary(10)

#print getBit(3, 17)

#print getPartialValue(1,3,22)