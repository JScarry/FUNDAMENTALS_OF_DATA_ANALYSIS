from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

mu = 0
sigma = 0.1
sns.distplot(random.normal(mu, sigma, 1000), hist=True)

plt.show()