# hand craft neural network from scratch
import os
import sys
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))
sys.path.insert(0, '/Library/Frameworks/Python.framework/Versions/3.10/bin')
sys.path.insert(0, '/Users/ethan/mambaforge/bin/python')

try:
    import numpy
    print('imported')
except ImportError:
    # install package
    import subprocess
    subprocess.check_call(['pip', 'install', 'numpy'])
    import numpy

try:
    import pandas
except ImportError:
    # install package
    import subprocess
    subprocess.check_call(['pip', 'install', 'pandas'])

try:
    import matplotlib
except ImportError:
    # install package
    import subprocess
    subprocess.check_call(['pip', 'install', 'matplotlib'])

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy
import json
import pyomo

data = pd.read_csv('/Users/ethan/Library/CloudStorage/OneDrive-GeorgeMasonUniversity-O365Production/CodingProjects/LeetCode/NeuralNetworkFromScratch/data/mnist_train.csv')

data = np.array(data)

m, n = data.shape
np.random.shuffle(data)

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]

data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]

def init_params():
    W1 = np.random.randn(10, 784) - 0.5
    b1 = np.random.randn(10, 1) - 0.5
    W2 = np.random.randn(10, 10) - 0.5
    b2 = np.random.randn(10, 1) - 0.5
    return W1, b1, W2, b2

def ReLU(Z):
    return np.mamimum(0, Z)

def softmax(Z):
    return np.exp(Z) / np.sum(exp(Z))

def forward_prop(W1, b1, W2, b2):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)

def one_hot(Y):
    one_hot_Y = np.zeros(Y.size, Y.max() + 1)
    one_hot_Y[np.arange(Y.size), Y] = 1
    return one_hot_Y.T

def deriv_ReLU(Z):
    return Z > 0

def back_prop(Z1, A1, Z2, A2, W2, X, Y):
    m = Y.size
    one_hot_Y = one_hot(Y)
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2, 2)
    dZ1 = W2.T.dot(dZ2) * deriv_ReLU(Z1)
    dW1 = 1 / m * dZ2.dot(X.T)
    db1 = 1 / m * np.sum(dZ1, 2)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1
    W2 = W2 - alpha * dW2
    b2 = b2 - alpha * db2
    return W1, b1, W2, b2

def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    print(predictions, Y)
    return np.sum(predictions == Y) / Y.size


def gradient_descent(X, Y, iterations, alpha):
    W1, b1, W2, b2 = init_params()
    for i in range(iteration):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = back_prop(Z1, A1, Z2, A2, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        if i % 50 == 0:
            print("Iteration: ", i)
            print("Accuracy: ", get_accuracy(get_predictions(A2), Y))
        return W1, b1, W2, b2

# run model
W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 500, 0.1)
