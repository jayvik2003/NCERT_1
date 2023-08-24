import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#for no money back
#100 samples
simlen=int(1e2)

#One event is taking 4 balls from bag with replacement
#Probability of the event that non of the balls are zero i.e pX(0)=(0.9)^4 which is denoted by 0 in the simulation
prob1 = (0.5)**3

#Generating sample date using Bernoulli r.v.
data_bern1 = bernoulli.rvs(size=simlen,p=prob1)
#Calculating the number of favourable outcomes
err_ind1 = np.nonzero(data_bern1 == 1)
#calculating the probability
err_n1 = np.size(err_ind1)/simlen

#Simulation Vs Theory  
print("Simulated for no money back = ",err_n1,"Theorical for no money back = ",prob1)
print(data_bern1)
print("\n")

#for double money back
#100 samples

#One event is taking 4 balls from bag with replacement
#Probability of the event that all tosses are heads i.e pY(1)=(0.5)^3 which is denoted by 1 in the simulation
prob2 = (0.5)**3

#Generating sample date using Bernoulli r.v.
data_bern2 = bernoulli.rvs(size=simlen,p=prob2)
#Calculating the number of favourable outcomes
err_ind2 = np.nonzero(data_bern2 == 1)
#calculating the probability
err_n2 = np.size(err_ind2)/simlen

#Simulation Vs Theory  
print("Simulated for double money back = ",err_n2,"Theorical for double money back = ",prob2)
print(data_bern2)
print("\n")

#for one time money back
err_n3 = 1-err_n1-err_n2
prob3 = 1-prob1-prob2
print("Simulated for single money back = ",err_n3,"Theorical for single money back = ",prob3)
