#! /user/bin/env Python3
#coding: utf-8

import argparse

import analysis.csv as c_an
import analysis.xml as x_an

 
def parse_arguments():
	# we must create an instance of "ArgumentParser" object 
	parser = argparse.ArgumentParser() 
	# we want to add an argument with 'add_argument' attribute of "ArgumentParser" Object
	parser.add_argument("-e","--extension",help = """ Type of file to analyse. Is it a CSV or a XML?""")
	# we return parsed arguments  
	return parser.parse_args() 


def main():
	# we call parse_argumetns()
	args = parse_arguments()
	if args.extension == 'csv':
		c_an.launch_analysis('current_mps.csv')
	elif args.extension == 'xml':
		x_an.launch_analysis('current_mps.csv')



if __name__ == '__main__':
	main()