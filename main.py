import random
import matplotlib.pyplot as plt
from node import Node 

class Graph:
    
    def __init__(self):
        # defines structure of the graph
        # nodeNum: Node -> {1: Node1, 2: Node2, ...}
        self.structure = {} 

    def construct(self, fileName):
        # we assume the graph is undirected
        # read the graph from file: node - its neighbor
        f = open(fileName, 'r')

        # construct graph -> parse the file and append the neighbors
        i = 0
        for line in f:
            if( i < 4):
                i+=1
                continue
            
            try:
                u, v = map(int,line.split())
            except:
                print('Parsing Error')

            if u not in self.structure:
                self.structure[u] = Node()

            if v not in self.structure:
                self.structure[v] = Node()

            self.structure[v].neighbors.append(u)
            self.structure[u].neighbors.append(v)

    def calculateDegrees(self):
        sum_degrees = 0 # the sum of the degrees of all nodes

        # calculate degree of each node and find sum of the degrees
        for node in self.structure.keys():
            self.structure[node].calculateDegree()
            sum_degrees += self.structure[node].degree

        # calculate normalized degree of each node
        for node in self.structure.keys():
            self.structure[node].calculateDegreeNorm(sum_degrees)

    def randomWalk(self, steps):
        L1_distance = 0
        currentPoint = random.choice(list(self.structure.keys())) # randomly choose a starting point
    
        for step in range(steps):
            # list of all node's neigbors
            variants = self.structure[currentPoint].neighbors

            if len(variants) == 0: continue # skip if no neighbors

            currentPoint = random.choice(variants) # next step
            self.structure[currentPoint].m_v += 1 # increment the number of visits for chosen node

        for node in self.structure.keys():
            # calculate empirical frequency vector and L1 distance as metrics
            self.structure[node].f_v =  self.structure[node].m_v / steps
            L1_distance += abs(self.structure[node].degreeNorm - self.structure[node].f_v)

        L1_distance = round(L1_distance, 3)
        print('With M = {} | L1 Distance = {}'.format(steps, L1_distance))
        return L1_distance

if __name__ == '__main__':
    fileName = 'com-dblp.txt'

    result = []
    baseStep = 10**7
    M = [baseStep, 2*baseStep, 3*baseStep, 4*baseStep, 5*baseStep]
    for steps in M:
        graph = Graph()
        graph.construct(fileName)
        graph.calculateDegrees()
        result.append(graph.randomWalk(steps))

    plt.plot(M, result)
    plt.show()