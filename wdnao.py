import numpy as np
import timeit

n=10 #lungimea cuvantului
k=10 #target de cuvinte
word=np.zeros(10)
code=['A','T','C','G']

wordsset=np.zeros((k,n))

m1=np.zeros((3,n))
m2=np.zeros((3,n))
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

def count (x,y):
	s=0
	if constrsA(x):
		s=s+1
	if constrsB(x,y):
		s=s+1
	if constrsB(rev(x),y):
		s=s+1
	return s

def countset (m):
	i=0
	s=0
	while i<n:
		j=i+1
		while j<n :
			s=s+(count(wordsset[i],wordsset[j]))
			j=j+1
		i=i+1
	return s

def genS (w):
	s = np.zeros((3,n))
	i=0
	poz=np.random.randint(n)
	while i<3:
		for j in range (1,4):
			c=np.zeros(n)
			for it in range(n):
				c[it]=w[it]
			c[poz]=(c[poz]+j)%4
			s[i]=c[:]
			i=i+1
	return s

def main():

	start_time = timeit.default_timer()
	i=0
	global wordsset
	while i<k:
		word=np.random.randint(4, size=n)
		wordsset[i]=word
		i=i+1

	i=0
	corr = 0
	while i<10000:
		x,y = np.random.randint(k),np.random.randint(k)
		if condition(wordsset[x],wordsset[y])==False & x!=y:
			m1 = genS(wordsset[x])
			m2 = genS(wordsset[y])
			if np.random.randint(2)==0:
				wordsset[x]=m1[np.random.randint(3)]
				c=wordsset
				wordsset[x]=np.random.randint(4, size=n)
				#print c[x], wordsset[x], countset(c),countset(wordsset)
				if countset(c)<countset(wordsset):
					wordsset=c
			else:
				wordsset[y]=m2[np.random.randint(3)]
				c=wordsset
				wordsset[y]=np.random.randint(4, size=n)
				#print countset(c),countset(wordsset)
				if countset(c)>countset(wordsset):
					wordsset=c
		else:
			corr=corr+1
		i=i+1

	elapsed = timeit.default_timer() - start_time


	print "No of ok " + str(corr) 
	print "Time " + str(elapsed)

	

main ()