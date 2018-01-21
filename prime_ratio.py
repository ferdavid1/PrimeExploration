import numpy as np 
import matplotlib.pyplot as plt 
from sympy import primerange
import mpl_toolkits.mplot3d.axes3d as p3

def find_prime_ratio(dataset_length):
	
	x = list(np.random.randn(dataset_length))
	primes = list(primerange(0, len(x))) 
	prime_subx = [x[i] for i in primes]
	x_hole = [i for i in x if i not in prime_subx]
	return len(x)/len(x_hole)

def plot(step, iterations, dataset_length, three_d=False):
	
	lengths = []
	ratios = []
	for x in range(iterations):
		lengths += [dataset_length]
		ratio = find_prime_ratio(dataset_length)
		ratios += [ratio]
		dataset_length += step
	if not three_d:
		plt.figure()
		plt.xlabel("Ratio")
		plt.ylabel("Size of dataset")
		plt.plot(ratios, lengths)
		plt.savefig("Primes_N_size.png")
		plt.show()

	else:
		fig = plt.figure()
		ax = p3.Axes3D(fig)
		ax.plot(ratios, lengths, list(range(iterations)))
		ax.set_xlabel("Ratio")
		ax.set_ylabel("Size of Dataset")
		ax.set_zlabel("Iteration")
		plt.savefig("Primes_3D.png")
		plt.show()

plot(100, 100, 1, three_d=True)
'''
phase transition? linear to log
# plot in 3d the iterations as z!
'''