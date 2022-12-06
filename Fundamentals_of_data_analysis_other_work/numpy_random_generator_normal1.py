import numpy as np

mu, sigma = 0, .1 # mean and standard deviation
#s = np.random.default_rng().normal(mu, sigma, 50)
s = np.random.normal(mu, sigma, 50)
abs(mu - np.mean(s))
1  # may vary

abs(sigma - np.std(s, ddof=1))
0.0  # may vary

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()