#!/usr/bin/python3
#Author: Dhruv Desai

#This is the code for printing traingle on screen
#The size and type is dependent on command line arguments
#
#Usage: python3 print_triangle <type: 0 for right, 1 for equilateral> <no. of rows>
#       Both the arguments are optional. 

#in branch

#edited the file from github UI, essentially a location other than my terminal

#Now the programming starts. Will keep above comments for historic reasons

#function to print triangle. Parameters are type and number of rows
def print_triangle(triangle, rows):
	stars=1
	while (rows):
		if (triangle):
			for i in range(rows - 1):
				print (" ", end="")
			for i in range(2*stars -1):
				print("*", end="")
		else:
			#for i in range(stars):
			for i in range(2*stars -1):
				print("*", end="")
		print()
		stars += 1
		rows -= 1

#main program starts here
import sys

triangle = 0 # variable to hold choice of right or equilateral 
rows = 3 # variable to hold number of rows

#print("Commandline arguments", sys.argv)

#if user has given command line parameters, do sanity check and assign it to correspoinding varibles
#or stick to default values
if (len(sys.argv) == 1):
	print ("Usage: python3 print_triangle <type: 0 for right, 1 for equilateral> <no. of rows>")
	print ("Taking default values")

if (len(sys.argv) > 1):
	if(sys.argv[1].isdigit()):
		triangle = int(sys.argv[1])
		if ( triangle != 0 and triangle != 1):
			triangle = 0

if (len(sys.argv) > 2):
	if(sys.argv[2].isdigit()):
		rows = int(sys.argv[2])
	
print ("Type of triangle", triangle, "No. of rows", rows)

#call function to print triangle
print_triangle(triangle, rows)
#end


