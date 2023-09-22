import numpy as np
from math import comb
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
#Sample size
simlen = 10000
n=5
for k1 in range(1,6):
#Probability of the event 
    prob1 = comb(5,k1)*(((4/5)**k1)*((1/5)**(5-k1)))
#Generating sample date using Bernoulli r.v.
    data_bern1 = bernoulli.rvs(size=simlen,p=prob1)
#Calculating the number of favourable outcomes
    err_ind1 = np.nonzero(data_bern1 == 1)
#calculating the probability
    err_n1 = np.size(err_ind1)/simlen
    print(err_n1)
