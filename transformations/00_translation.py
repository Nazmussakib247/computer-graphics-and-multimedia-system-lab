import numpy as np
import matplotlib.pyplot as plt
P=np.array([[0,0],[2,0],[1,2],[0,0]])
T=np.array([3,2])
Q=P+T
plt.plot(P[:,0],P[:,1],label='original'); plt.plot(Q[:,0],Q[:,1],label='translated')
plt.legend(); plt.axis('equal'); plt.grid(True); plt.show()
