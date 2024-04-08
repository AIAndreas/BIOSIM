import numpy as np
import random 
from MPNeuron_Assignment1 import MPNeuron

input = np.array([[0,0],[1,0],[0,1],[1,1]])
target = np.array([0,1,1,1])
weights =  np.random.rand(1, 4)
r = 1
E = 100
it = 0
while E >= 0.00001:
    output = np.zeros(4)
    for i in range(4):
        output[i] = MPNeuron(input[i, :])
    perception_output = output * weights
    perception_output = perception_output[0]
    if not np.array_equal(perception_output,target):
        for i in range(4):
            w_delta = r*(sum(target - perception_output))*perception_output[i]
            weights[0,i] = weights[0,i] + w_delta
    E = abs(sum(target - perception_output))
    it += 1
    print("Iteration: ", it, "Perception Output: ", perception_output, "Error: ", E, "Weights: ", weights)
