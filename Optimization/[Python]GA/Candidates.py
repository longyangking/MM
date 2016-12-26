import numpy as np
import random

class Candidates(object):
    def __init__(self,popsize,chromsize,fitnessfun):
        self.popsize = popsize
        self.chromsize = chromsize
        self.fitnessfun = fitnessfun
        self.fitness = np.zeros([popsize])
        self.chroms = np.zeros([popsize,chromsize])
        self.randinit()
        self.fit()

    def randinit(self):
        self.chroms = np.random.randint(2,size=(self.popsize,self.chromsize)) 

    def mutate(self,pmutate):
        temp = self.chroms.reshape(self.popsize*self.chromsize,1)
        self.chroms = np.array(map(lambda x:self.__mutateChrome(x,pmutate),temp)).reshape(self.popsize,self.chromsize)

    def __mutateChrome(self,x,pmutate):
        if random.random() < pmutate:
            return (x+1)%2
        return x

    def cross(self,pcross):
        #for i in range(self.popsize):
        #    if random.random() < pcross:
        #        father = random.randint(0,self.popsize-1)
        #        mother = random.randint(0,self.popsize-1)
        #        while father == mother:
        #            mother = random.randint(0,self.popsize-1)
        #        crossChrome = random.randint(0,self.chromsize-lencross-1)
        #        
        #        gene = self.chroms[father][crossChrome:crossChrome+lencross-1]
        #        self.chroms[father][crossChrome:crossChrome+lencross-1] = self.chroms[mother][crossChrome:crossChrome+lencross-1]
        #        self.chroms[mother][crossChrome:crossChrome+lencross-1] = gene
        newchroms = np.zeros([self.popsize,self.chromsize])
        newpopsize = 0
        while newpopsize < self.popsize:
            if random.random() < pcross:
                father = self.__selection()
                mother = self.__selection()
                while father == mother:
                    mother = self.__selection()
                
                crossChromeStart = random.randint(0,self.chromsize-1)
                if crossChromeStart is not self.chromsize-1:
                    crossChromeEnd = random.randint(crossChromeStart+1,self.chromsize-1)
                else:
                    crossChromeEnd = self.chromsize               

                gene = self.chroms[father][crossChromeStart:crossChromeEnd]
                self.chroms[father][crossChromeStart:crossChromeEnd] = self.chroms[mother][crossChromeStart:crossChromeEnd]
                self.chroms[mother][crossChromeStart:crossChromeEnd] = gene

                newchroms[newpopsize] = self.chroms[father]
                newchroms[newpopsize + 1] = self.chroms[mother]

                newpopsize = newpopsize + 2

        self.chroms = newchroms

    def __selection(self):
        totalfitness = np.sum(self.fitness)
        fitnessorder = np.argsort(-self.fitness)
        prob = random.random()
        sum = 0
        for i in range(self.popsize):
            sum = sum + self.fitness[fitnessorder[i]]/totalfitness
            if sum > prob:
                return i

        #print self.fitness
        #print fitnessorder
        return fitnessorder[0]
    
    def fit(self):
        for i in range(self.popsize):
            self.fitness[i] = self.fitnessfun(self.chroms[i])

    #def eliminate(self,size):
    #    '''
    #    Leave size of best candidates and regenerate new generation in popsize-size
    #    '''
    #    self.fit()
    #    fitnessorder = np.argsort(-self.fitness)
    #    bestchroms = np.zeros([size,self.chromsize])
    #    for i in range(size):
    #        bestchroms[i] = self.chroms[fitnessorder[i]]
    #    self.randinit() #All left will be regenerated randomly
    #    for i in range(size):
    #        self.chroms[i] = bestchroms[i]

    def getcandidate(self,index):
        self.fit()
        fitnessorder = np.argsort(-self.fitness)
        return self.chroms[fitnessorder[index]]

    def getallcandidate(self):
        return self.chroms
