#!/usr/bin/python3
#Author: Dhruv Desai

#This is the code for printing traingle on screen
#The size and type is dependent on command line arguments
#
#Usage: python3 print_triangle -h
#       

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
#import argparse for using readymade argument parsing
#tutorial at https://docs.python.org/3/howto/argparse.html

import argparse
parser = argparse.ArgumentParser(description='A simple program to print triangles. Without arguments, it will print a right angled triangle with 3 rows')
parser.add_argument("-t","--triangle", help="Provide type of triangle r|right, e|equilateral", choices=['right', 'r', 'equilateral', 'e']) 
parser.add_argument("-r","--row", help="Provide number of rows", type=int)

args= parser.parse_args()

triangle = 0 # variable to hold choice of right or equilateral. Default is right angle
rows = 3 # variable to hold number of rows. Default is 3 rows

#print("Commandline arguments", sys.argv)

#if user has given command line parameters, do sanity check and assign it to correspoinding varibles
#or stick to default values

if args.triangle == 'equilateral' or args.triangle == 'e':
	triangle = 1

if args.row is not None:
	rows = args.row
	
print ("Type of triangle", triangle, "No. of rows", rows)

#call function to print triangle
print_triangle(triangle, rows)
#end


