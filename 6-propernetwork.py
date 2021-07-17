# create a proper neural network to classify 00,01,10,11 to 0,1,2,3

# importing numpy library
import numpy as np


# Relu(Rectified logic unit) function
def relu(x):
    return np.max(x, 0)


def forward_propagation(x, w1, w2, b1, b2):
    z1ws = np.dot(x, w1.T)  # weighted sum
    print("Z1 weighted sum:",z1ws)
    z1 = z1ws+b1  # weigth sum plus bias
    print("Z1 weighted sum + bias:",z1)

    a1 = relu(z1)  # relu activation function
    print("Output:", a1)

    a1 = np.transpose(a1)  # transpose a1
    
    z2ws = np.dot(a1, w2.T)
    print("Z2 weighted sum:",z2ws)

    z2 = z2ws+b2
    print("Z2 weighted sum + bias:",z2)

    a2 = relu(z2)
    print("Output:", a2)

    return a1, a2


x = np.array([1, 1])  # input array
x.shape = (1, 2)
print("input array: "+str(x))

w1 = np.array([[2.5, 3.5], [1.6, 4.6], [3.7, 2.7]])  # weight array 1
print("W1:" + str(w1))

w2 = np.array([1, 1, 1])  # weight array 2
print("W2:"+str(w2))

b1 = 2.9  # bias 1
b2 = 3.1  # bias 2
forward_propagation(x, w1, w2, b1, b2)  # main function
