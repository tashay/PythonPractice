import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")

v = np.array([3,7])

plt.arrow(0,0,v[0],v[1], head_width=0.8, head_length=0.8)
plt.axis([0,5,0,10])
plt.show()
