import os
from GA import GA
from utils import routeFitness
import warnings
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt 

def readNetwork1(filename):
    net = {}
    with open(filename, 'r') as file:
        
        net['noNodes'] = int(file.readline())

        net['mat'] = [[0 for i in range(net['noNodes'])] for j in range(net['noNodes'])] 

        for i in range(0, net['noNodes']):
            splits = file.readline().split(',')
            for j in range(0, net['noNodes']):
                net['mat'][i][j] = int(splits[j])

    return net

def readNetwork2(filename):
    net = {}
    with open(filename, 'r') as file:
        
        net['noNodes'] = int(file.readline())

        distante = [[0,0,0] for i in range(net['noNodes'])] 

        for i in range(0, net['noNodes']):
            splits = file.readline().split(' ')
            for j in range(3):
                distante[i][j] = float(splits[j])

        net['mat'] = [[0 for i in range(net['noNodes'])] for j in range(net['noNodes'])] 

        for i in range(0, net['noNodes']):
            for j in range(0, net['noNodes']):
                xDis = abs(distante[i][1] - distante[j][1])
                yDis = abs(distante[i][2] - distante[j][2])
                distance = ((xDis ** 2) + (yDis ** 2))**0.5
                net['mat'][i][j] = distance

    return net

def main():

    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'hardE.txt')
    
    #network = readNetwork1(filePath)
    network = readNetwork2(filePath)

    gaParam = {'popSize' : 100, 'noGen' : 100}
    problParam ={'network': network,'function':routeFitness}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    best = []    
    for g in range(gaParam['noGen']):

        #ga.oneGenerationElitism()
        ga.oneGenerationSteadyState()
        bestChromo = ga.bestChromosome()
        print('Generatia de platina ' + str(g) + ' este: x = ' + str(bestChromo.repres) + '\nf(x) = ' + str(bestChromo.fitness) + '\nDistanta = ' + str(bestChromo.distance))
        best.append(bestChromo.distance)

    plt.plot(best)
    plt.ylabel('Lungime minima')
    plt.xlabel('Generatie')
    plt.show()

main()

