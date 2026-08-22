import numpy as np
import matplotlib.pyplot as plt
P=np.array([[0,0],[3,0],[2,2],[0,0]])
S=np.array([[1.5,0],[0,0.75]])
Q=P@S.T; M=np.array([[-1,0],[0,1]])
R=Q@M.T
plt.plot(P[:,0],P[:,1],label='original'); plt.plot(Q[:,0],Q[:,1],label='scaled'); plt.plot(R[:,0],R[:,1],label='reflected')
plt.legend(); plt.axis('equal'); plt.grid(True); plt.show()
