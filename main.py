import random
import matplotlib.pyplot as plt
import seaborn as sns
from node import Node 

### Utils ###
from utils.metrics import l1_distance
from graph import Graph

def relationship(nodes, M):
    degreeNormList = []
    freqList = []
    for node in nodes:
        degreeNormList.append(node.degreeNorm)
        freqList.append(node.f_v)
    plt.title('{} steps'.format(M))
    plt.xlabel('n')
    plt.ylabel('f')
    plt.scatter(degreeNormList, freqList)
    plt.show()

if __name__ == '__main__':
    fileName = 'data/com-dblp.txt'


    sub = 'non_stopping_nodes' # Monte Carlo for stoping
    
    graph = Graph()
    graph.construct(fileName)
    graph.calculate_PageRank_PowerIteration()
    ground_truth = graph.getPageRank() # ground truth vector

    result = []
    for i in [2,4,6,8,10]:
        PageRank_vector = graph.calculate_PageRank_RandomWalk(i*graph.getSize(), sub)
        diff = l1_distance(ground_truth, PageRank_vector)
        print('For M = {}*n, difference = {}'.format(i, diff))
        result.append(diff)
    
    plt.figure();
    plt.xlabel('M')
    plt.ylabel('Difference')
    sns.lineplot(x = [2,4,6,8,10], y = result);
    plt.show()