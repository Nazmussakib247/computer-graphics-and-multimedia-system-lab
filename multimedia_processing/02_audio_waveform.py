import numpy as np
import matplotlib.pyplot as plt
rate=44100; duration=2; t=np.linspace(0,duration,rate*duration,endpoint=False)
signal=.6*np.sin(2*np.pi*440*t)+.25*np.sin(2*np.pi*660*t)
plt.plot(t[:2000],signal[:2000]); plt.title('Synthetic audio waveform'); plt.xlabel('time (s)'); plt.ylabel('amplitude'); plt.grid(); plt.show()
