import sys
sys.path.append('..')

from GA import GA
import math
import numpy as np

def fitfun(chrome):
    n = len(chrome)
    num = 0
    #for i in range(n):
    #    if chrome[i] is 1:
    #        num = num + 10
    return 10*sum(chrome)

if __name__=='__main__':
    ga = GA(30,20,fitfun,probcross=0.8,probmutate=0.2,lencross=2,maxiteration=100,bestspliter=5)
    ga.start()
    print sum(ga.result(0))