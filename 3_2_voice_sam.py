#02.02.2019
# to record sound --- arecord -d time -r rate >filename.format
#
import scipy.io.wavfile as w
import numpy as np
import matplotlib.pyplot as plt

fs,data = w.read('tuning_fork.wav')
k  = len(data)
t = np.linspace(0,k/fs,k)
plt.figure(1)
plt.plot(t,data)
plt.figure(2)
a = np.fft.fft(data)
#freq = np.fft.fftfreq(t.shape(-1))
plt.plot(a)
plt.show()

