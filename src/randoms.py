
import numpy as np
import matplotlib.pyplot as plt

c_size = 10000

r1 = np.random.uniform(0, 10, size=c_size)
r2 = np.random.uniform(0, 10, size=c_size)
r3 = np.random.uniform(0, 10, size=c_size)

# plt.hist(r1, bins=100)
plt.hist(r1 + r2 + r3, bins=100)
plt.show()

