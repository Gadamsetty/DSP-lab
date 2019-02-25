
import numpy as np
def convolute(x,h):
	n1 = len(x)
	n2 = len(h)
	y = []
	for n in range(n1+n2-1):
		sum = 0 
		for k in range(n1):
			if ((n-k>=0)&(n-k<=n2-1)):
				sum = sum +(x[k]*h[n-k])
		y = np.append(y,sum)
	return y

def time_rev(h):
	l = len(h)
	hr = []
	for i in range(l):
		hr.append(h[l-i-1])
	return hr

def corr(x,h):
	hr = time_rev(h)
	y = convolute(x,hr)
	return y
	
	
	
x = input("x")
h = input("x")
hr = time_rev(h)
y1 = convolute(x,h)
y2 = corr(x,h)
print(hr)
print(np.convolve(x,h))
print(y1)
print(y2)


