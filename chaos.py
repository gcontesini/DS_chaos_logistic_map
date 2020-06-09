#!/usr/python3

import numpy as np
import math 

def main():

	def f(x,r):
		return(r*x*(1.0-x))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	for i  in np.arange(0,400,1):
		
		aux=0.5
		r=(i)/(100.0)

		for j in np.arange(100):

			print j,"\t",aux,"\t"
			aux=f(aux,r)

		print "\n"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	# series = np.arange(70)
	
	# for i  in np.arange(0,400,1):
		
	# 	r=((i+1e-5)/(400.0))
	# 	freq=0
	# 	aux=0.5
		
	# 	for j in np.arange(70):
	
	# 		series[j]=aux*1.0
	# 		aux=f(aux,r)
		
	# 	freq=np.fft.hfft(series)

	# 	for k in np.arange(35):
	
	# 		print k,freq[k]
	
	# 	print "\n"
	

if __name__ == '__main__':
	main()