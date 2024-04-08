import numpy as np


def MPNeuronMAX3(input):
    sum = np.sum(input)
    if len(input) > 3: # More than 3 inputs return error
        raise ValueError
    if sum >= 1:
        return 1
    else:
        return 0


def MPNeuron(input):
    sum = np.sum(input)
    if sum >= 1:
        return 1
    else:
        return 0