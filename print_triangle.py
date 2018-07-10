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

#referring to https://pymotw.com/3/configparser/ for help
from configparser import ConfigParser
from pathlib import Path

#name(with location) of configuration file
CONFIGFILE='./triangle.conf'

triangle = 0 # variable to hold choice of right or equilateral. Default is right
rows = 3 # variable to hold number of rows. Default is 3

#print("Commandline arguments", sys.argv)

#if user has given command line parameters, do sanity check and assign it to correspoinding varibles
#or stick to default values

my_file = Path(CONFIGFILE)

if(my_file.is_file()):
	parser = ConfigParser()

	#pass the strict=False argument if sections with same name needs to be ignored
	#parser = ConfigParser(strict=False)
	
	parser.read(CONFIGFILE)
	
	#check if the TRIANLGE section is present
	if(parser.has_section('TRIANGLE')):
		section = parser['TRIANGLE']
		
		#check if option in the section is present
		if(parser.has_option('TRIANGLE', 'type')):
			#check if the value is equilateral. For rest, its default value of right
			if(section['type'] == 'equilateral'):
				triangle = 1

		#check if options in the section are present
		if(parser.has_option('TRIANGLE', 'rows')):
			#check if the value is digit
			if(section['rows'].isdigit()):
				rows = parser.getint('TRIANGLE','rows')
	
print ("Type of triangle", triangle, "No. of rows", rows)

#call function to print triangle
print_triangle(triangle, rows)
#end


