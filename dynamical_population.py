import sys
import matplotlib.pyplot as plt


def main():
	""" This script reads in order three parameters: initial population, final t, scalar r
	and print a list and plot the population growth, i.e. f(t) where t=0,...,t_final,
	with the recurrence relation: f(t+1)=r*f(t)*[1-f(t)].
	"""
	assert len(sys.argv)==4, "Script expected three parameters:" + str(len(sys.argv)-1)
	script = sys.argv[0]
	x = float(sys.argv[1])
	final_t = int(sys.argv[2])
	r = int(sys.argv[3])
	population=iterate(x,final_t,r)
	print(population)
	plt.plot(range(0,final_t),population, label='Population[t]')
	plt.legend()
	plt.xlabel('Time (t)')
	plt.show()

def iterate(initial_pop, final_t, r):
	""" This function makes the iteration over the range [0,t_final]
	"""
	results=[initial_pop]
	pop=initial_pop
	for i in range(1,final_t):
	  results.append(logistic_map(pop,r))
	  pop = logistic_map(pop,r)
	return results
	
def logistic_map(pop, r=1):
	""" This function takes the population at time t: f(t) 
	and calculates it  at time t+1: f(t+1), where
	f(t+1)=r*f(t)*[1-f(t)]
	"""
	npop=r*pop*(1-pop)
	return npop

if (__name__=='__main__'):
	main()
