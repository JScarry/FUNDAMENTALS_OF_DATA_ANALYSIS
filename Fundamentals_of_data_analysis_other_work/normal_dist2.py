import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm as norm
import statistics as st
  
# Plot between -10 and 10 with .001 steps.
x = ([625, 600, 500, 400, 300, 200, 100, 0])
y = ([1324, 1988, 12133, 16189, 12865, 7544, 3623, 2268])

plt.bar(x, y)  
# Calculating mean and standard deviation
#mean = st.mean(x_axis)
#sd = st.stdev(x_axis)
  
#plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
#plt.show()
#plt.hist(x_axis, bins = 20)
plt.show()
