#!/usr/bin/env python3

# You will be supplied with two data files in CSV format.
# The first file contains statistics about various dinosaurs. 
# The second file contains additional data.
# Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)
# Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
# Do not print any other information.

import csv
import math

# create a dinosaur class 
class Dinosaur():
	def __init__(self, name, leg_length, diet, stride_length, stance):
		self.name = name
		self.leg_length = leg_length
		self.diet = diet
		self.stride_length = stride_length
		self.stance = stance
		self.speed = (float(stride_length)/float(leg_length)-1)* math.sqrt(float(leg_length))*9.8

# create a function that read from two csv files
def dinosaursFromCsv(filename1, filename2):
	dinosaurArr = []
	# read the first csv
	with open(filename1,newline='') as csvfile1:
		reader1 = csv.DictReader(csvfile1)
		for row1 in reader1:
			# assign values to dinosaur attributes from csv files and append to list
			dinosaurArr.append(Dinosaur(row1['NAME'],row1['LEG_LENGTH'],row1['DIET'],0.0,0.0))

	# read the second csv
	with open(filename2,newline='') as csvfile2:
		reader2 = csv.DictReader(csvfile2)	
		for row2 in reader2:
			for x in dinosaurArr:
				if x.name == row2['NAME']:
					x.stride_length = row2['STRIDE_LENGTH']
					x.stance = row2['STANCE']
	return dinosaurArr

# call the function to create an object list				
dinosaurObjs = dinosaursFromCsv('dataset1.csv','dataset2.csv')
# sort the list by speed
dinosaurObjs.sort(key=lambda dinosaur:dinosaur.speed, reverse=True)

# print name of dinosaur which stance is 'bipedal'
for dinosaurObj in dinosaurObjs:
	if dinosaurObj.stance == 'bipedal':
		print(dinosaurObj.name)
