#Id Number:R151734
#Name : Gadamsetty Sai Prakash
#Class :T-06
#9.generate and plot bpsk signal for 1000110101 and plot its magnitude spectrum
import numpy as np
import matplotlib.pyplot as plt
import cmath

j = cmath.sqrt(-1)

def discrete_ft(a):
	a = np.asarray(a)
	len_aa = a.shape
	len_a = len_aa[0]      #since shape is tuple of length we take only row element count by accessing first value of tuple
	p = np.pi
	w = np.linspace(-p,p,3000)
	l=3000
	y = np.zeros((l,),dtype = complex)
	for k in range(l):
		s = 0
		for m in range(len_a):
			s = s+(a[m]*(np.exp(-(m*j*w[k]))))
		y[k]=s
	return y

def bpsk_gen(s):
	s = np.asarray(s)
	bpsk_sig =[]

	t = np.linspace(0,2,100)

	cos_0 = np.cos(2*np.pi*t)
	cos_pi = np.cos((2*np.pi*t)+np.pi)

	for i in s:
		if (i == 1):
			bpsk_sig = np.append(bpsk_sig,cos_0)
		else:
			bpsk_sig = np.append(bpsk_sig,cos_pi)
	return bpsk_sig
	

seq = np.array([1,0,0,0,1,1,0,1,0,1])
bpsk_signal = bpsk_gen(seq)

wp = np.linspace(0,40*np.pi,1000)
plt.figure(1)
plt.plot(wp,bpsk_signal)
plt.title("bpsk signal for 1000110101")
#freqency response
p = np.pi
wf = np.linspace(-p,p,3000)
bpsk_frqres = discrete_ft(bpsk_signal)
mag = np.abs(bpsk_frqres)

plt.figure(2)
plt.plot(wf,mag)
plt.title("magnitude response of bpsk signal")
plt.xlabel("--->frequency in rad/sec")
plt.ylabel("--->magnitude")

plt.show()



