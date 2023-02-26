# hand craft neural network from scratch
import os
import sys
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))
sys.path.insert(0, '/Library/Frameworks/Python.framework/Versions/3.10/bin')

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

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
