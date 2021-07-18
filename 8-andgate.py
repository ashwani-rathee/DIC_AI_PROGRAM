# create a proper neural network to classify 00,01,10,11 

# importing numpy library
import numpy as np
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal
  
# sigmoid function
def sigmoid(x):
    return 1/(1+np.exp(-x))

x1 = 0
x2 = 1

w1 = np.random.random()
w2 = np.random.random()
w3 = np.random.random()
w4 = np.random.random()
w5 = np.random.random()
w6 = np.random.random()
w7 = np.random.random()
w8 = np.random.random()
w9 = np.random.random()

b1 = np.random.random()
b2 = np.random.random()
b3 = np.random.random()
b4 = np.random.random()

z1 = 0
z2 = 0
z3 = 0

a1 = 0
a2 = 0
a3 = 0

z4 = 0

a4 = 0
losses = []
def plotgraph(name ,x = range(1,10000), y = losses):
    # Data for plotting
    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='Steps(i)', ylabel='Loss(loss)',
        title='Loss Vs Steps')
    ax.grid()

    fig.savefig("{}.png".format(name))
    plt.show()
    return 

def forwardpropagation(x1,x2,w1,w2,w3,w4,w5,w6,w7,w8,w9,b1,b2,b3,b4):
    global z1, z2, z3, z4, a1, a2, a3, a4
    z1 = w1*x1 + w4*x2 + b1
    z2 = w2*x1 + w5*x2 + b2
    z3 = w3*x1 + w6*x2 + b3

    a1 = sigmoid(z1)
    a2 = sigmoid(z2)
    a3 = sigmoid(z3)

    z4 = w7*a1 + w8*a2 + w9*a3 + b4

    a4 = sigmoid(z4)


def backwardpropagation(expected_output):
    global w1, w2, w3, w4, w5, w6, w7, w8, w9, b1, b2, b3, b4
    global z1, z2, z3, z4, a1, a2, a3, a4

    # calculating derivative of loss function
    dl_da4 = -(expected_output - a4)

    # calculating derivative of sigmoid function
    dl_dz4 = dl_da4 * a4 * (1-a4)

    dl_db4 = dl_dz4
    dl_dw7 = dl_dz4 * a1
    dl_dw8 = dl_dz4 * a2
    dl_dw9 = dl_dz4 * a3

    dl_da1 = dl_dz4*w7
    dl_da2 = dl_dz4*w8
    dl_da3 = dl_dz4*w9

    dl_dz1 = dl_da1*a1*(1-a1)
    dl_dz2 = dl_da2*a2*(1-a2)
    dl_dz3 = dl_da3*a3*(1-a3)

    dl_db1 = dl_dz1
    dl_db2 = dl_dz2
    dl_db3 = dl_dz3

    dl_dw1 = dl_dz1*x1
    dl_dw2 = dl_dz2*x1
    dl_dw3 = dl_dz3*x1

    dl_dw4 = dl_dz1*x2
    dl_dw5 = dl_dz2*x2
    dl_dw6 = dl_dz3*x2
    
    lr = 1
    w1 = w1 - lr*dl_dw1
    w2 = w2 - lr*dl_dw2
    w3 = w3 - lr*dl_dw3
    w4 = w4 - lr*dl_dw4
    w5 = w5 - lr*dl_dw5
    w6 = w6 - lr*dl_dw6
    w7 = w7 - lr*dl_dw7
    w8 = w8 - lr*dl_dw8
    w9 = w9 - lr*dl_dw9

    b1 = b1 - lr*dl_db1
    b2 = b2 - lr*dl_db2
    b3 = b3 - lr*dl_db3
    b4 = b4 - lr*dl_db4

    loss = 0.5*(expected_output - a4)**2
    return loss


for i in range(1,10000):
    dataset = [[0,0,0],[0,1,0],[1,0,0],[1,1,1]]
    print("Step:",i)
    i = np.random.randint(0,4)
    x1 = dataset[i][0]
    x2 = dataset[i][1]
    expected_output = dataset[i][2]
    # print("x1: ",x1,"x2: ",x2,", expected_output: ",expected_output)
    forwardpropagation(x1,x2,w1,w2,w3,w4,w5,w6,w7,w8,w9,b1,b2,b3,b4)
    loss = backwardpropagation(expected_output)
    losses.append(loss)
    print("Loss :{0:.3f}".format(loss))
    if loss == 0:
        break

# plotgraph("And") # graph of loss versus steps

while(True):
    x1 = int(input("Enter x1 : "))
    x2 = int(input("Enter x2 : "))
    forwardpropagation(x1,x2,w1,w2,w3,w4,w5,w6,w7,w8,w9,b1,b2,b3,b4)
    print(x1,x2,w1,w2,w3,w4,w5,w6,w7,w8,w9,b1,b2,b3,b4)
    print("Output : {0:.3f}".format(a4))

