import numpy as np
import random 
from MPNeuron_Assignment1 import MPNeuron



def MPNeuron(input, weights):
    g = np.sum(input * weights)
    sigmoid = 1/(1+np.exp(-g))
    return 


input = np.array([[0,0],[1,0],[0,1],[1,1]])
target = np.array([0,1,1,1])
weights =  np.random.rand(4, 2)
print(weights)
r = 1
E = 100
it = 0
while E >= 0.00001:
    output = np.zeros(4)
    for i in range(2):
        output[i] = MPNeuron(input[i, :], weights)
    perception_output = output
    print(perception_output)
    if not np.array_equal(perception_output,target):
        for i in range(2):
            w_delta = r*(sum(abs(target - perception_output)))*perception_output[i]
            weights[0,i] = weights[0,i] + w_delta
            # print(weights)
    E = abs(sum(target - perception_output))
    it += 1
    if it > 100:
        print("Iteration: ", it, "Perception Output: ", perception_output, "Error: ", E, "Weights: ", weights)
        break
    print(it)
    print("Iteration: ", it, "Perception Output: ", perception_output, "Error: ", E, "Weights: ", weights)
