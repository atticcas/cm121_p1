#!/usr/bin/python
import math
import numpy
from math import log
from math import exp

def safe_log(x):
    if x == 0:
        return float("-inf")
    else: 
        return math.log(x)

def log_add(logA,logB):
    if logB > logA:
        return log_add(logB,logA)
    #print "input: ", logB,logA
    #return numpy.logaddexp(logA,logB)+log(logA)
    #print "log sum: ",log(1+exp(logB-logA)) + logA
    return log(1+exp(logB-logA)) + logA

print log_add(math.log(10),math.log(12))
#function used to compute variant scores score for each of the variant sites in the input data. 
#using variant scoring model
#sequence can be either normal(S) or mutant (S')
#takes in S and Sc as a list of the same individual read on the same spot
def basic_score(S,Sc):
    sum_all_mutate = 0 #theta = 0.2
    sum_all_unmutate = 0 #theta = 0
    p_S = 0
    p_Sc = 0.2 
    for list_s, list_sc in zip(S,Sc):
        #print list_s, S[list_s],Sc[list_sc]
        #both s and sc are log10 based need to switch to ln base first 
        #based on log10(P) = ln(P)/ln10
        for s, sc in zip(S[list_s],Sc[list_sc]):
            x = s*log(10)   #x is p(obs|S)
            y = sc*log(10)  #y is p(obs|S')
            #print "theta = 0.2", y+safe_log(p_Sc), " ", x+safe_log(1-p_Sc)
            #print "theta = 0", y+safe_log(p_S), " ", x+safe_log(1-p_S)
            #print log_add(y+safe_log(p_Sc),x+safe_log(1-p_Sc))
            #print log_add(y+safe_log(p_S),x+safe_log(1-p_S))
            #sum_all_mutate = log_add(sum_all_mutate,log_add(y+safe_log(p_Sc),x+safe_log(1-p_Sc)))
            #sum_all_unmutate = log_add(sum_all_mutate,log_add(y+safe_log(p_S),x+safe_log(1-p_S)))
            sum_all_mutate += log_add(y+safe_log(p_Sc),x+safe_log(1-p_Sc))
            sum_all_unmutate += log_add(y+safe_log(p_S),x+safe_log(1-p_S))
    print "theta = 0.2: ", sum_all_mutate, "exp: ",exp(sum_all_mutate)
    print "theta = 0: ", sum_all_unmutate, "exp: ",exp(sum_all_unmutate)
    return sum_all_mutate-sum_all_unmutate
        


def test_main():
    for x in range(1,11):
        s = "seq.%d.txt" % (x)
        f = open(s,'r')
        list_S = {}#dict 
        list_Sc = {}
        l = [] #denote which individuals have already been added 
        for line in f:
            values = line.split("\t")
            if values[0] not in l:
                l.append(values[0])
                list_S[int(values[0])] = [float(values[1])]
                list_Sc[int(values[0])] = [float(values[2].strip("\n"))]
            else:
                list_S[int(values[0])].append(float(values[1]))
                list_Sc[int(values[0])].append(float(values[2].strip("\n")))
        print "site: ", x
        print basic_score(list_S,list_Sc)
        f.close()

test_main()
