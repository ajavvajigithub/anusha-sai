import numpy as np
import math

def fermatNearMiss():

	#prompts user to enter value for n and if the constraints are not met prompts user to re-enter
	n = int(input("n :"))

	while n <= 2 or n >= 12:
		print("\nn value should be greater than 2 and less than 12\n")
		x = int(input("x :"))

	#prompts user to enter value for k and if the constraints are not met prompts user to re-enter
	k = int(input("k :"))
	while k <= 10:
		print("\nk value should be greater than 10\n")
		k = int(input("k :"))

	#initialize miss to a large value
	miss = math.inf

	#compute for all x,y permutations
	for x in range(10, k+1):
		for y in range(10, k+1):
			X = np.power(x,n)
			Y = np.power(y,n)
			Z = X+Y

			z = np.power(Z,(1/n))
			z1 = int(math.floor(z))
			z2 = int(math.ceil(z))

			difference1 = np.power(z2, n) - Z
			difference2 = Z - np.power(z1,n)

			difference = min(difference1, difference2)
			if difference == difference1:
				ztemp = z1
			else:
				ztemp = z2

			#check if relative miss is smaller than existing miss
			if difference/Z < miss:
				miss = difference/Z
				print("X: ",x, " Y: ",y, " Z: ", ztemp, " Actual miss: ", difference, " Fractional miss: ", miss)

#invoke the function
fermatNearMiss()