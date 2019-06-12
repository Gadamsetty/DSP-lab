#Remove 50Hz powerline interference from given ECG signal, ‘ ecg.txt ’ with the help of
#fir notch or bandstop filter.(fs=1000Hz)

import numpy as np 
import matplotlib.pyplot as plt
import scipy.signal as sig

fs = 1000
fo = 50
q = 25

#file opening and processing
f = open("ecg.txt","r")
ecg = f.readline()
ecg_data = ecg.split()
print(len(ecg_data))
e  = []
k = 0
for i in ecg_data:
    e.append(float(i))

f.close()

#filter designing and filtering

b,a = sig.iirnotch(fo,q,fs)       #returns the numerator and denominator coefficients of transfer function
freq,h = sig.freqz(b,a,fs=fs)   #returns the impulse response

y = sig.lfilter(b,a,e)   #function that performs filtering


plt.figure(1)
plt.plot(y)
plt.title("after removing 50 hz")
plt.figure(2)
plt.plot(e)
plt.title("before filtering")
plt.show()
