class Node:
    def __init__(self):
        self.neighbors = [] #node neighobrs
        self.degree = 0 # number of neighobrs
        self.degreeNorm = 0 # normalized degree of the node
        self.m_v = 0 # number of times the node was visited
        self.f_v = 0 # empirical frequency vector

    def calculateDegree(self):
        self.degree = len(self.neighbors)

    def calculateDegreeNorm(self, sum_degrees):
        self.degreeNorm = self.degree / sum_degrees