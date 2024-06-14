import numpy as np
import matplotlib.pyplot as plt

n = 10
p = 0.5
size_bin = 5

binomial_data = np.random.binomial(n, p, size_bin)

mu = 2
sigma = 0.1
size = 5

normal_data = np.random.normal(mu, sigma, size)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

axes[0].hist(binomial_data, bins=10)
axes[0].set_title("Binomial Distribution")
axes[0].set_xlabel("Bins")
axes[0].set_ylabel("Values")



axes[1].hist(normal_data, bins=10)
axes[1].set_title("Normal Distribution")
axes[1].set_xlabel("Bins")
axes[1].set_ylabel("Values")
fig.suptitle('Binomial and Normal Distributions with N=5', fontsize=16)
plt.show()


n = 10
p = 0.5
size_bin = 1000

binomial_data = np.random.binomial(n, p, size_bin)

mu = 2
sigma = 0.1
size = 1000

normal_data = np.random.normal(mu, sigma, size)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

axes[0].hist(binomial_data, bins=10)
axes[0].set_title("Binomial Distribution")
axes[0].set_xlabel("Bins")
axes[0].set_ylabel("Values")



axes[1].hist(normal_data, bins=10)
axes[1].set_title("Normal Distribution")
axes[1].set_xlabel("Bins")
axes[1].set_ylabel("Values")
fig.suptitle('Binomial and Normal Distributions with N=1000', fontsize=16)
plt.show()





