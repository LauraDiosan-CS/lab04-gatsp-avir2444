from random import randint
import Chromosome

def init_repres(problParam):
    repres = [0]

    while (len(repres) < problParam['noNodes']):
        city = randint(1, problParam['noNodes']-1)     
        if (city not in repres):
            repres.append(city)

    repres.append(0)
    return repres

def routeFitness(c):
    fitness = 1 / float(c.routeDistance())
    return fitness