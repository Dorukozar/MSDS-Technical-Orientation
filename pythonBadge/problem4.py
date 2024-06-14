import numpy as np
import matplotlib.pyplot as plt

n = 10
p = 0.5
size_bin = 1000

binomial_data = np.random.binomial(n, p, size_bin)


lamb = 4
size_pos = 10000
poisson_data = np.random.poisson(lamb, size_pos)

mu = 2
sigma = 0.1
size = 1000

normal_data = np.random.normal(mu, sigma, size)

plt.hist(binomial_data, bins=10)
plt.title("Binomial Distribution")
plt.xlabel("Bins")
plt.ylabel("Values")
plt.show()


plt.hist(poisson_data, bins=10)
plt.title("Poisson Distribution")
plt.xlabel("Bins")
plt.ylabel("Values")
plt.show()


plt.hist(normal_data, bins=10)
plt.title("Normal Distribution")
plt.xlabel("Bins")
plt.ylabel("Values")
plt.show()





