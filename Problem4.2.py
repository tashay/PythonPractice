import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")

v = np.array([3,7])
vLong = v*2

plt.arrow(0,0,v[0],v[1], head_width=0.8, head_length=0.8,color ='grey', linestyle = '--')
plt.arrow(0,0,vLong[0],vLong[1], head_width=0.8, head_length=0.8)
plt.axis([0,10,0,20])
plt.show()
