import numpy as np
import matplotlib.pyplot as plt
P=np.array([[0,0],[3,0],[2,2],[0,0]])
a=np.deg2rad(35); R=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
Q=P@R.T
plt.plot(P[:,0],P[:,1],label='original'); plt.plot(Q[:,0],Q[:,1],label='rotated')
plt.legend(); plt.axis('equal'); plt.grid(True); plt.show()
