import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as w


def disctft(a):
	a = np.asarray(a)
	l_aa = a.shape
	l_a = l_aa[0]
	print l_a
	p = np.pi
	w = np.linspace(0j,6.286j,1000)
	l=1000
	y = np.zeros((l),dtype = complex)
	for k in range(l):
		s = 0
		for m in range(l_a):
			s = s+(a[m]*(np.exp(-(p*m*w[k]))))
		y[k]=s
	return y

a = np.array(input("enter "))
w = np.linspace(0,6.286,1000)

b = disctft(a)

b_m = np.abs(b)
b_p = np.angle(b)
print b_m
plt.figure(1)
plt.plot(w,b_m)
plt.figure(2)
plt.plot(w,b_p)
plt.show()

