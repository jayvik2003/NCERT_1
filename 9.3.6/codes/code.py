import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli


#100 samples
simlen=int(100)

#Probability of the event 
prob1 = (4/5)**4

#Generating sample date using Bernoulli r.v.
data_bern1 = bernoulli.rvs(size=simlen,p=prob1)
#Calculating the number of favourable outcomes
err_ind1 = np.nonzero(data_bern1 == 1)
#calculating the probability
err_n1 = np.size(err_ind1)/simlen

#probability of four out of five students being swimmers Simulation  Vs Theory  
print("Simulated = ",err_n1,"Theorical = ",prob1)
print(data_bern1)
print("\n")
