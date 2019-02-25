#02.02.2019
# to record sound --- arecord -d time -r rate >filename.format
#
import scipy.io.wavfile as w
import numpy as np
import matplotlib.pyplot as plt

r,d = w.read('eee_48000.wav')
w.write('eee_8000.wav',8000,d)
w.write('eee_96000.wav',96000,d)
print r
#k = len(d)
#r2,d2 = w.read('eee_8000.wav')
#print r2
#.figure(1)
plt.plot(d)
#plt.figure(2)
#plt.plot(d2)
plt.show()
