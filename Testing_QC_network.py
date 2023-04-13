#import network for graph tools
import networkx as nx

#improt dwave_nework for dwave functions
import dwave_networkx as dnx

#import matplotlib to draw graphs
import matplotlib.pyplot as plt

#set the solver
from dwave.system.smaplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler(profile = 'webinar'))

#crate empty graph
G = nx.Graph()

# add edges to graph
#G.add_edges_from([(1,2),(1,3),(2,3),(3,4),(3,5),(4,5),(4,6),(5,6),(6,7)])

G.add_edges_from([(1,2),(1,3),(1,7),(2,4),(2,5),(4,8),(5,11),(8,11),(3,6),(6,9),(9,11),(7,10)(10,11)])

#find the max indep. set
S = dnx.maximum_independent_set(G,sampler = sampler, num_reads = 10)

# print the solution for the user
print('Maximum independent set size found is:' , len(S))
print(S)

##visualize the result

k = G.subgraph(S)
notS = list(set(G.nodes())-set(S))
othersubgraph = G.subgraph(notS)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G,pos = pos)
nx.draw(k, pos = pos)
nx.draw(othersubgraph, pos = pos, node_color = 'b')
plt.show()