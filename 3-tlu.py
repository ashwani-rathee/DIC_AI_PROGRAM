# create a threshold logic unit
import numpy as np

x = [1,2,3]
w = [0.1,0.5,0.3]
z = np.dot(x, w)

print("Z(weighted sum) :>", z)

# create a step function
def step(x):
	if x >= 2:
		return x
	else:
		return 0

hw = step(z)

print("Hw(x) = step(x) :> ",hw)



######

# heavyside step function

def hstep(x):
	if z>=0:
		return 1
	else:
		return 0


#####

# sgn(x) function

def sgn(x):
	if z>0:
		return 1
	elif z = 0:
		return 0
	else 
		return -1

######