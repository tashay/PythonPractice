import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
import math

def rotMatrix(angle):
    return np.array([[np.cos(np.radians(angle)), -np.sin(np.radians(angle))], [np.sin(np.radians(angle)), np.cos(np.radians(angle))]])

v = np.array([3,7])
v30 = rotMatrix(np.deg2rad(-30)).dot(v)

plt.arrow(0,0,v[0],v[1], head_width=0.8, head_length=0.8, color ='grey', linestyle = '--')
plt.arrow(0,0,v30[0],v30[1],head_width=0.8, head_length=0.8)
plt.axis([0,5,0,10])
plt.show()



