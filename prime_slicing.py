import numpy as np 
import matplotlib.pyplot as plt 
from sympy import primerange
from scipy.stats import ks_2samp, kstest # kolmogorov-smirnov test, for two distributions

x,y = list(np.random.randn(300)), list(np.random.randn(300))
primes = list(primerange(0, len(x))) 
prime_subx, prime_suby = [x[i] for i in primes], [y[i] for i in primes]
x_hole = [i for i in x if i not in prime_subx]
y_hole = [i for i in y if i not in prime_suby]

def plot():
	fig = plt.figure()
	ax = p3.Axes3D(fig)
	ax.scatter(x,y, 6) # also could use ax.scatter
	ax.scatter(prime_subx, prime_suby, 4)
	ax.scatter(x_hole, y_hole, 2)
	plt.show()

plot()