#!/usr/bin/python3
#Author: Dhruv Desai

#This is the code for printing traingle on screen
#The size and type is dependent on optional configuration file triangle.conf in the same directory
#In absence of config file or desired section, a right angled triangle with 3 rows will be printed
#Both the parameters are optional. Single valid option will be entertained
#
#Format of triangle.conf
#[TRIANGLE]
#	type = <equilateral|right>
#	rows = <no of rows in digits
#
#For example
#[TRIANGLE]
#        type = equilateral
#        rows = 25

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

#referring to https://pymotw.com/3/configparser/ for help
from configparser import ConfigParser
from pathlib import Path

#name(with location) of configuration file
CONFIGFILE='./triangle.conf'

triangle = 0 # variable to hold choice of right or equilateral. Default is right
rows = 3 # variable to hold number of rows. Default is 3

#if config file is present, do sanity check and assign values to correspoinding varibles
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


