# create a multilayer perceptron

import numpy as np

x = np.array([0.5, 1])
w = np.array([[2, 3], [1, 4], [3, 2]])
b = np.array([0.1, 0.6, 0.9])

# multiply x to each element in w and create a array
xw = np.multiply(x,w) 
print(xw)
# [[1.  3. ]
#  [0.5 4. ]
#  [1.5 2. ]]

# create a new array which is sum of xw row wise
ws = np.sum(xw,axis=1)  
print(ws)
# [4.  4.5 3.5]


# add biases to ws elementwise wb = ws[0] + b[0]
wb = np.add(ws, b)
print(wb)
# [4.1 5.1 4.4]
