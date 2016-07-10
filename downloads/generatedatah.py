"""
Function to generate sample data for analysing the births children
Data is useful for understanding the variance in weight, and height of 
children born based on the gender of the child
"""
import numpy as np
import pandas as pd
import os

def generate_birth_data(rndSeed):
	# Generte weight data
	np.random.seed(int(rndSeed))

	data_size = 0
	while(data_size < 2000 or data_size > 4000):
		data_size = int(2000 * np.random.random() + 2000)

	girl = 'girl,'
	Gal = 'Gal,'
	Girl = 'Girl,'
	Boyz = 'Boyz,'
	boy = 'boy,,'
	gir = 'gir,'
	gril = 'gril,'
	byo = 'byo,'
	num_reg = int(np.floor(data_size/4.))
	num_ireg = int(np.floor(data_size/6.))
	num_ireg2 = int(np.floor(data_size/3.))
	girls = (girl * num_reg).split(',')[:-1]
	boys = (boy * num_reg).split(',')[:-1]
	Gals = (Gal * num_ireg).split(',')[:-1]
	Girls = (Girl * num_ireg).split(',')[:-1]
	Boyzs = (Boyz * num_ireg).split(',')[:-1]
	girs = (gir * num_ireg2).split(',')[:-1]
	grils = (gril * num_ireg2).split(',')[:-1]
	byos = (byo * num_ireg2).split(',')[:-1]

	Gender = girls + boys + Gals + Girls + Boyzs + girs + grils + byos
	np.random.shuffle(Gender)
	num_weights = len(Gender)
	weight_ireg = int(np.floor(num_weights * 0.25))
	weight_reg = num_weights - (2 * weight_ireg)
	weight_high = np.random.randint(21, 122, weight_ireg)
	weight_low = np.random.randint(0,17,weight_ireg)/10.0
	weight_norm = np.random.randint(18,42, weight_reg)/10.0
	Weights = np.hstack((weight_high, weight_norm, weight_low))
	np.random.shuffle(Weights)
	Height = np.random.randint(38,60,num_weights)
	BirthDay = []
	ChildCondition = []

	dates = pd.date_range('1/1/2002', periods=720, freq='D')
	conditions = ['Healthy, Tall', 'Weak, Tall, Hairy', 'Tall', 'Weak, Healthy', 'Normal, Healthy']
	for i in range(num_weights):
		BirthDay.append(dates[np.random.randint(0,719)])
		ChildCondition.append(conditions[np.random.randint(0,4)])

	return Gender, Weights, Height, BirthDay, ChildCondition

if __name__ == '__main__':
	stdNum = 708
	#print generate_birth_data(stdNum)