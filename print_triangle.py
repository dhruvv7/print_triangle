#!/usr/bin/python3
#Author: Dhruv Desai

#This is the code for printing traingle on screen
#The size and type is dependent on command line arguments
#
#Usage: python3 print_triangle <size_in_integer> <type: 0 for right, 1 for equilateral>
#       Both the arguments are optional. 

#in branch

#edited the file from github UI, essentially a location other than my terminal

#Now the programming starts. Will keep above comments for historic reasons

import sys

triangle = 0 # variable to hold choice of right or equilateral 
rows = 3 # variable to hold number of rows

#if user has given command line parameters, do sanity check and assign it to correspoinding varibles
#or stick to default values
if (sys.len > 0):
	temp = int(sys.argv[0]) #convert to int

	if (isinstance(temp,int) == True) #check if temp is indeed int
		triangle = temp

	if ( triangle != 0 || triangle != 1)
		triangle = 0


print (sys.argv)

#call function to print triangle

#end

#function to print triangle. Parameters are type and number of rows
