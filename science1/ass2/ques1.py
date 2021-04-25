# so I need a sequence worth of 1000 having 4 numbers



import random
import math

proteins_with_more_than_240 = 0

for a in range(10000):
	protein = []
	number_of_A = 0
	for i in range(1000):
		base = math.floor(random.uniform(0 , 4))
		if base == 0 :
			number_of_A = number_of_A + 1


	if number_of_A >= 240:
		proteins_with_more_than_240 = proteins_with_more_than_240 + 1





print("The approx prob of getting at least 240 A's as per code is " +  str( round(float(proteins_with_more_than_240/10000)  , 7)) )