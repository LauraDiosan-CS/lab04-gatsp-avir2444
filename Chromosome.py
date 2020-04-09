from random import randint
import random
from utils import init_repres

class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        self.__repres = init_repres(problParam)
        self.__fitness = 0.0
        self.__distance = 0
    
    @property
    def repres(self):
        return self.__repres
    
    @property
    def fitness(self):
        return self.__fitness
    
    @property
    def distance(self):
        return self.__distance 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 

    @distance.setter
    def distance(self, d = 0):
        self.__distance = d 

    def crossover(self, c):

        childP1 = []
        childP2 = []
        childP3 = []

        geneA = randint(1, self.__problParam['noNodes']-1)
        geneB = randint(1, c.__problParam['noNodes']-1)
    
        startGene = min(geneA, geneB)
        endGene = max(geneA, geneB)

        childP1 = self.__repres[startGene : endGene+1]
        
        childP2 = [item for item in c.__repres[endGene+1 : -1] if item not in childP1]

        childP3 = [item for item in c.__repres[1 : endGene+1] if item not in childP1]

        childP1.extend(childP2)

        i = 0
        while(len(childP1) < self.__problParam['noNodes'] - endGene + startGene - 1):
            childP1.append(childP3[i])
            childP3.remove(childP3[i])

        childP3.extend(childP1)
        childP3.append(0)
        childP3.insert(0, 0)

        offspring = Chromosome(self.__problParam)
        offspring.repres = childP3
        return offspring

    def mutation(self):

        swapWith = random.randint(1,self.__problParam['noNodes']-1)
        swapped = random.randint(1,self.__problParam['noNodes']-1)

        city1 = self.__repres[swapped]
        city2 = self.__repres[swapWith]
            
        self.__repres[swapped] = city2
        self.__repres[swapWith] = city1
        
    def routeDistance(self):
        pathDistance = 0
        for i in range(0, len(self.__repres)):
            fromCity = self.__repres[i]
            toCity = 0
            if i + 1 < len(self.__repres):
                toCity = self.__repres[i + 1]
            else:
                toCity = self.__repres[0]
            pathDistance += self.__problParam['mat'][fromCity][toCity]
        distance = pathDistance
        self.distance = distance
        return distance

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
