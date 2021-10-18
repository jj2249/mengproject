import numpy as np
import matplotlib.pyplot as plt
from sys import argv
from functions import *

def gen_gamma_process(c, beta, rate, samps, maxT=1):
	# generate a set of poisson epochs
	es = gen_poisson_epochs(rate, samps)
	
	# jump sizes - QUITE UNSTABLE ATM
	x = 1.0/(beta*(np.exp(es/c)-1))
	# acceptance probabilities
	acceps = (1+beta*x) * np.exp(-beta * x)
	# keep selected samples
	accepted = accept(x, acceps)

	# independently generated jump times
	times = maxT*np.random.rand(samps)
	#sort jumps
	times_sorted, jumps = sort_jumps(times, accepted)

	# return gamma process - SHOULD (0,0) be set as the first value??
	gamma_process = np.cumsum(jumps)

	return times_sorted, gamma_process