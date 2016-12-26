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
    return sum(chrome)

if __name__=='__main__':
    ga = GA(30,10,fitfun,probcross=0.8,probmutate=0.1,maxiteration=200)
    ga.start()
    print fitfun(ga.result(0))