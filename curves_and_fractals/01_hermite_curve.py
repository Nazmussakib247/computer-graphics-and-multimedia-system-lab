import numpy as np
import matplotlib.pyplot as plt
p0=np.array([0.,0.]); p1=np.array([5.,2.]); m0=np.array([3.,5.]); m1=np.array([3.,-4.])
t=np.linspace(0,1,400)[:,None]
h00=2*t**3-3*t**2+1; h10=t**3-2*t**2+t; h01=-2*t**3+3*t**2; h11=t**3-t**2
C=h00*p0+h10*m0+h01*p1+h11*m1
plt.plot(C[:,0],C[:,1]); plt.scatter(*zip(p0,p1)); plt.title('Cubic Hermite curve'); plt.grid(); plt.axis('equal'); plt.show()
