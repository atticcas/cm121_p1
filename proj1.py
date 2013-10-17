import math
import numpy
from math import log

def safe_log(x):
	if x == 0:
		return float("-inf")
	else: 
		return math.log(x)

def log_add(logA,logB):
    if logB > logA:
        return log_add(logB,logA)
    #return numpy.logaddexp(logA,logB)+log(logA)
    return log(1+exp(logB-logA)) + logA

print log_add(math.log(10),math.log(12))
#function used to compute variant scores score for each of the variant sites in the input data. 
#using variant scoring model
#sequence can be either normal(S) or mutant (S')
def basic_score(S,Sc):
    p_S = 0
    p_Sc = 0.2 
    print S
    print Sc


for x in range(1,11):
	s = "seq.%d.txt" % (x)
	f = open(s,'r')
	l = []
	for line in f:
		values = line.split("\t")
		#if values[0] not in l:
		l.append(values[0])
		#for value in values:
		#	print value.strip()
	test = []
	for value in l:
		value = int(value)
		test.append(value)
	test.sort()
	f.close()
print test
print len(test)

	
