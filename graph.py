import random
from utils.metrics import l1_distance

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
    
    def renew(self):
        for node in self.structure.values():
            node.pageRank = 0

    def getSize(self):
        return len(self.structure)
    
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

    def calculate_PageRank_PowerIteration(self, max_iterations = 10 ** 20, alpha = 0.15, eps = 10**(-9)): 
        # initialize PageRank vector pi^0 as {1/n}
        x = {}
        for key, node in self.structure.items():
            node.pageRank = 1/self.getSize()
            x[key] = 1/self.getSize()

        i = 0
        while i <= max_iterations:
            i += 1
            xlast = x
            x = {}
            for key, node in self.structure.items():
                x[key]=(1-alpha)*sum(self.structure[v].pageRank*(1/len(self.structure[v].neighbors)) 
                                        for v in node.neighbors)+alpha*(1/self.getSize())
            
            for key, value in x.items():
                self.structure[key].pageRank= value

            err = l1_distance(x, xlast)
            if err <= eps:
                print('Power Iteration Method | Vector used as ground truth')
                print(f'Number of iterations until convergence: {i}') 
                print(f'Final error: {err}')
                break

    def calculate_PageRank_RandomWalk(self, M, sub, alpha = 0.15):

        visiting_nodes = [0]*self.getSize()
        terminating_nodes = [0]*self.getSize()

        for i in range(M):
            node = random.randint(0,self.getSize()-1)
            visiting_nodes[node]+=1
            factor = random.random()
            while factor>alpha:

                node = random.choice(self.structure[node].neighbors)
                visiting_nodes[node]+=1
                factor = random.random()

            terminating_nodes[node]+=1

        if sub == 'stopping_node_only':
            page_rank = {node: terminating_nodes[node]/M for node in self.structure}
        elif sub == 'non_stopping_nodes':
            page_rank = {node: alpha*visiting_nodes[node]/M for node in self.structure}

        return page_rank

    def getPageRank(self):
        returnList = {}
        for key, node in self.structure.items():
            returnList[key] = node.pageRank

        return returnList