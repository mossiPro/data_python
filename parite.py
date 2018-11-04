#! /user/bin/env Python3
#coding: utf-8

import analysis.csv as c_an
import analysis.xml as x_an


if __name__ == '__main__':
	c_an.launch_analysis('current_mps.csv')
	x_an.launch_analysis('current_mps.csv')