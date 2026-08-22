import numpy as np
import matplotlib.pyplot as plt
P=np.array([[0,0],[1,3],[4,3],[5,0]])
t=np.linspace(0,1,400)[:,None]
B=(1-t)**3*P[0]+3*(1-t)**2*t*P[1]+3*(1-t)*t**2*P[2]+t**3*P[3]
plt.plot(B[:,0],B[:,1]); plt.plot(P[:,0],P[:,1],'--o'); plt.title('Cubic Bezier curve'); plt.grid(); plt.axis('equal'); plt.show()
