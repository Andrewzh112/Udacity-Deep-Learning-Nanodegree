import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    e_sum = np.sum(np.exp(L))
    return np.exp(L) / e_sum