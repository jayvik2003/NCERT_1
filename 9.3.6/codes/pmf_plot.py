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
    sim=np.array([0.0,0.0,0.0,0.0,0.0,0.0])
    sim[k1]=err_n1
    print(k1)
print(sim)


#Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
#plt.stem(n,panal, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()# minor

#If using termux
plt.savefig('/home/jay/Desktop/ncert1/9.3.6/codes/pmf.pdf')
plt.savefig('/home/jay/Desktop/ncert1/9.3.6/codes/pmf.png')
#subprocess.run(shlex.split("termux-open figs/pmf.pdf"))
#else
plt.show()
