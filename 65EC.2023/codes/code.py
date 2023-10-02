import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = np.arange(1,9)   # Number of trials
p = ([1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128, 1/128]) # Probability of success

mu = np.sum(n * p) #minimum entropy

print(mu)

