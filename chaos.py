# Time Series of the logistic map evolving from predictable
# to chaotic "This is useless!"

import numpy as np

def main():

	f = lambda x, r : r*x*(1.0-x)

	for i  in np.arange(0,400,1):

		aux=0.5
		r=(i)/(100.0)

		for j in np.arange(100):

			print j,"\t",aux,"\t"

			aux = f( aux, r)

		print "\n"

if __name__ == '__main__':
	main()
