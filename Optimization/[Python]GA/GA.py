from Candidates import Candidates
import numpy as np

class GA(object):
    def __init__(self,popsize,chromsize,fitnessfun,probcross=0.8,probmutate=0.1,maxiteration=100):
        self.popsize = popsize
        self.chromsize = chromsize
        self.candidates = Candidates(popsize,chromsize,fitnessfun)
        self.fitnessfun = fitnessfun
        self.probcross = probcross
        self.probmutate = probmutate
        self.maxiteration = maxiteration

    #def originalgeneration(self):
    #    self.candidates.randinit()
    #    self.candidates.fit()

    #def newgeneration(self):
    #    '''
    #    Genetic Cross and Mutation
    #    '''
    #    self.candidates.eliminate(self.bestspliter)

    def update(self):
        '''
        Select best Candidates
        '''
        #self.newgeneration() 
        self.candidates.fit()
        self.candidates.cross(self.probcross)
        self.candidates.mutate(self.probmutate)

    def start(self):
        #self.originalgeneration()
        for iter in range(self.maxiteration-1):
            #self.newgeneration()
            self.update()
        #self.newgeneration()

    def result(self,index):
        candidateindex = self.candidates.getcandidate(index)
        return candidateindex

    def finalcandidate(self):
        return self.candidates.getallcandidate()