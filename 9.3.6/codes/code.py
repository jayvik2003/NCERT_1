import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 5  
p = 0.8  
k = np.arange(0, n+1)  
binomial_pmf = binom.pmf(k, n, p)
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x = np.linspace(0, n, 1000)
normal_pdf = norm.pdf(x, mu, sigma)
plt.stem(k, binomial_pmf, label='Binomial PMF', basefmt='b-')
plt.plot(x, normal_pdf, label='Gaussian PDF', color='r')
plt.axvline(x=4, color='g', linestyle='--', label='x=4')
plt.xlabel('Number of Swimmer')
plt.ylabel('Probability')
plt.legend()
plt.savefig("/home/jay/Desktop/ncert1/9.3.6/figs/approx.png")
plt.show()
