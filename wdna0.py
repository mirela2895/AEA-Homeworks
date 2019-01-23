import numpy as np
import timeit

n=8 #lungimea cuvantului
k=100 #target de cuvinte
word=np.zeros(8)
code=['A','T','C','G']

wordsset=np.zeros((k,n))

# Word , Position , Letter
# Letters:
#  A = 0
#  T = 1
#  C = 2
#  G = 3

w=0

# Each word in S has n/2 symbols from { C,G };
def constrsA(w):
	s=0
	for p in range(n):
		if w[p]==0.:
			s=s+1
		if w[p]==1.:
			s=s+1
	
	if s>=n/2:
		return True
	else:
		return False

# Each pair of distinct words in S are the same in at most n/2 positions
def constrsB(x,y):
	s=0
	for p in range(n):
		if x[p]==y[p]:
			s=s+1
	
	if s<=n/2:
		return True
	else:
		return False

def transform(w):
	return w

def rev (w):
	x=np.zeros(n)
	x=w
	i=0
	while i<n:
		x[i]=int(x[i]/2)*2+(x[i]+1)%2
		i=i+1
	return x

def condition (x,y):
	if constrsA(x) & constrsB(x,y) & constrsB(y,rev(x)):
		return True
	else:
		return False

def main():
	start_time = timeit.default_timer()
	i=0
	global wordsset
	while i<k:
		word=np.random.randint(4, size=n)
		wordsset[i]=word
		i=i+1

	i=0
	corr=0
	while i<1000*k:
		x,y = np.random.randint(k),np.random.randint(k)
		if condition(wordsset[x],wordsset[y])==False & x!=y:
			if np.random.randint(2)==0:
				wordsset[x]=np.random.randint(4, size=n)
			else:
				wordsset[y]=np.random.randint(4, size=n)
		else:
			corr=corr+1
		i=i+1

	elapsed = timeit.default_timer() - start_time


	print "No of ok " + str(corr)
	print "Time " + str(elapsed)


main ()