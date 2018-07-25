#! /usr/bin/env python3

import numpy as np
import re

import matplotlib.pyplot as plt

if __name__ == '__main__':
    file = open('training_output/test.txt', 'r')

    iterations = np.array([], dtype=np.int)
    scores = np.array([])

    """
    This code parses the DL4J ScoreIterationListener output to extract the score
    data for each iteration
    """
    iteration_regex = re.compile("iteration ([0-9]*)")
    score_regex = re.compile("is ([0-9.E-]*)")
    for line in file:
        iteration = int(iteration_regex.search(line).group(1))
        iterations = np.append(iterations, iteration)
        score = float(score_regex.search(line).group(1))
        scores = np.append(scores, score)


    # create a running mean
    window_size = 15
    running_mean = np.convolve(scores, np.ones((window_size,))/window_size, mode='same')
    plt.plot(iterations, scores)
    plt.plot(iterations, running_mean)
    plt.xlabel('Example')
    plt.ylabel('Loss')
    plt.legend(['score', 'rolling mean'])
    plt.tight_layout()
    plt.show()

