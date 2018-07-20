#! /usr/bin/env python3

import numpy as np
import re

import matplotlib
matplotlib.use('WxAgg')
import matplotlib.pyplot as plt

import seaborn as sns

if __name__ == '__main__':

    fileName = 'histograms/hist_01.txt'

    data = None

    """
    This code parses the .txt file in DL4J format into a numpy array
    """
    comma_regex = re.compile(",(?=[0-9])")
    for line in open(fileName, 'r'):
        # replace decimal commata with decimal points
        line = re.sub(comma_regex, ".", line)
        # replace the array stuff
        line = line[2:-3]

        arrayLine = np.fromstring(line, sep=',')

        if data is None:
            data = arrayLine
        else:
            data = np.vstack((data, arrayLine))


    # rotate data befor plotting
    data = np.rot90(data, k=1)
    ax = sns.heatmap(data, cmap='inferno', xticklabels=10)
    # set the layer labels correctly
    ax.set_yticklabels([6, 5, 4, 3, 2, 1])
    ax.set_ylabel("Layer")
    ax.set_xlabel("Wire")
    plt.show()
    
