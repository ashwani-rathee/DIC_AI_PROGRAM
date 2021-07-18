# from here: https://towardsai.net/p/machine-learning/nothing-but-numpy-understanding-creating-neural-networks-with-computational-graphs-from-scratch-6299901091b0

# importing numpy library
import numpy as np
# x1 x2 y
# 0  0  0
# 0  1  1
# 1  0  1
# 1  1  1

x1 = 0
x2 = 0
w1 = 0.1
w2 = 0.6
b = 0.0
z =  x1*w1 + x2*w2 + b
y_hat = 1/ (1 + np.exp(-z))
y = 0
print("Y hat:",y_hat)
loss = 0.5*np.power(y - y_hat,2)
print("Loss:",loss)

def next_step(y, y_hat):
    dl_dyhat = y_hat -y
    dy_hat_dz = y_hat*(1-y_hat)
    dl_dz = dl_dyhat * dy_hat_dz
    dz_dw1 = x1
    dz_dw2 = x2
    dz_db = 1
    dl_dw1 = dl_dz*dz_dw1
    dl_dw2 = dl_dz*dz_dw2
    dl_db = dl_dz*dz_db
    # print("Derivative:",dl_dyhat)
    # print("Derivative dy_hat_dz:",dy_hat_dz)
    # print("Derivative dl_dz:",dl_dz)
    global b
    b = b - 0.5*dl_db
    w1 = b - 0.5*dl_dw1
    w2 = b - 0.5*dl_dw2

    z =  x1*w1 + x2*w2 + b
    y_hat = 1/ (1 + np.exp(-z))

    print("Y hat:",y_hat)
    y = 0
    loss = 0.5*np.power(y - y_hat,2)
    print("Loss:",loss)

for i in range(20):
    next_step(y,y_hat)



