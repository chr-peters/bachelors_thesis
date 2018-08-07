#! /usr/bin/env python3

import numpy as np
import re

import matplotlib
#matplotlib.use('WxAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import seaborn as sns

def get_data(fileName):
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

    return data
    

if __name__ == '__main__':

    fileName = 'validation/val_s2_sl2.txt'

    #baseline = get_data('histograms/baseline_signal.txt')
    #fuse_mask = get_data('histograms/channel_mask.txt')

    # add random dead wires
    #baseline[np.random.rand(112, 6) < 0.03] = 0

    # apply the mask to the data
    #baseline[fuse_mask > 0] = 0
    data = get_data(fileName)

    # rotate data befor plotting
    data = np.rot90(data, k=1)
    ax = sns.heatmap(data, cmap='hot', xticklabels=10)
    # set the layer labels correctly
    ax.set_yticklabels([6, 5, 4, 3, 2, 1])
    ax.set_ylabel("Layer")
    ax.set_xlabel("Wire")

    # create a rectangle to illustrate the region of interest
    # dead pin: rect = patches.Rectangle((14, 0.5), 12, 2, linewidth=2, edgecolor='blue', facecolor='none')
    # dead connector: rect = patches.Rectangle((27, 0), 8, 6, linewidth=2, edgecolor='blue', facecolor='none')
    # dead wire: rect = patches.Rectangle((80, 3.5), 9, 2, linewidth=2, edgecolor='blue', facecolor='none')
    # hot wire:
    #rect = patches.Rectangle((1, 1.5), 7, 2, linewidth=2, edgecolor='blue', facecolor='none')
    #rect = patches.Rectangle((60, 0), 24, 6, linewidth=2, edgecolor='blue', facecolor='none')
    #ax.add_patch(rect)
    
    plt.tight_layout()
    plt.show()
    
