import numpy as np
import matplotlib.pyplot as plt
window=np.array([[0,0],[10,0],[10,6],[0,6],[0,0]])
viewport=np.array([2,3])+window*np.array([1.5,1.0])
plt.plot(window[:,0],window[:,1],label='window'); plt.plot(viewport[:,0],viewport[:,1],label='viewport mapping')
plt.axis('equal'); plt.grid(); plt.legend(); plt.show()
