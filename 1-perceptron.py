# create a simple perceptron
import numpy as np

x = [1, 0, 1, 0, 1]
w = [0.1, 0.2, 0.3, 0.4, 0.5]
bias = 0.6

# sigmoid function
def sigmoid(x):
    return 1/(1+np.exp(-x))


y = sigmoid(np.dot(x, w)+bias)

print(y)
