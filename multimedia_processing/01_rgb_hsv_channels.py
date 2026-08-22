import numpy as np
import matplotlib.pyplot as plt
r=np.linspace(0,1,256); g=np.linspace(1,0,256); b=np.full(256,.5)
img=np.dstack([np.tile(r,(160,1)),np.tile(g,(160,1)),np.tile(b,(160,1))])
plt.subplot(1,4,1); plt.imshow(img); plt.title('RGB'); plt.axis('off')
for i,name in enumerate(['Red','Green','Blue']):
    channel=np.zeros_like(img); channel[:,:,i]=img[:,:,i]
    plt.subplot(1,4,i+2); plt.imshow(channel); plt.title(name); plt.axis('off')
plt.show()
