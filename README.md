### Graph Algos

Here I implemented several methods on an undirected graph graph:
    - Simulated a random walk and calculated the L1 distance between the normalized degree vector and  the empirical frequency vector; 

    - Calculated the PageRank of the graph (PowerIteration and Monte Carlo methods);

![condition](/ph/cond.png)

## Observations

With a fixed degree of a node (normalized degree of *v* is const), the L1 distance benween *n* (normalized degree) and *f* (empirical frequency vector) decreases when the *M*  - number of steps, increases. It decreases exponentially:

![condition](/ph/viz.png)


## Calculation of PageRank | *Power Iteration*

Provided the undirected graph, the method was implemented and the PageRank vector was calculated. 80 iterations were done until convergence (Epsilon is 1e-10). Update Rule:
![condition](/ph/PI_rule.png)

The given PageRank vector was used as ground truth to evaluate other methods.

## Calculation of PageRank | *Monte Carlo*

The calculated PageRank vector will be evaluated with Manhattan Distance metrics (calculated PageRank_1 vector).

### Monte Carlo 1 (with parameter sub == "stopping_node_only")

We can see that with increase in number of random walks *(M = 2n, 4n, 6n, 8n, 10n; where n is the number of nodes in the graph)* Manhattan Distance metric decreases:
![condition](/ph/r1.png)
![condition](/ph/m_graph1.png)

### Monte Carlo 2 (with parameter sub == "non_stopping_node")

In the above Monte Carlo method 1, we only used the stopping node to approximate PageRank which is
wasteful as all the non-stopping nodes in random walks are ignored. Let 𝑠𝑣 be the number of times that 𝑣
appears in the 𝑀 random walk. In this sub question 𝑠𝑣/M was used to estimate the PageRank value of 𝑣.




