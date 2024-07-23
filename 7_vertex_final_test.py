import copy
from sage.graphs.graph import Graph
from sage.sets.set import Set
from itertools import combinations

edge_list_W5 = [(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2)] #Wheel graph W5 (the only non-word-representable graph on 6 vertices)
Non_wr_6_vertex_graph=Graph(edge_list_W5)

#Following 26 graphs are the non-word-representable graphs on 7 vertices.
G1 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (3,7)]) 
G2 = Graph( [(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (4,7), (2,7)])
G3 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (4,7), (2,7), (3,7)])
G4 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (4,7), (2,7), (1,7)])
G5 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (1,7)])
G6 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (3,7), (1,7)])
G7 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (3,7), (2,7)])
G8 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (3,7), (2,7), (1,7)])
G9 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (3,7), (2,7), (5,7)])
G10 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (3,7), (2,7), (1,7), (5,7)])
G11 = Graph( [(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (3,7), (1,7), (2,7), (6,7)])
G12 = Graph( [(1,2), (1,3), (1,4), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (3,5), (3,6), (3,7), (2,7)])
G13 = Graph([(1,3), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (4,7), (2,7), (5,7), (6,7)])
G14 = Graph([(1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (4,7), (2,7), (5,7), (6,7)])
G15 = Graph( [(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (4,7), (2,7), (5,7), (6,7)])
G16 = Graph( [(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (1,7), (4,7), (2,7), (5,7), (6,7)])
G17 = Graph( [(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (2,4), (4,7), (2,7), (5,7), (6,7)])
G18 = Graph( [(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (3,7), (4,7), (2,7), (5,7), (6,7)])
G19 = Graph( [(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (1,7), (3,7), (4,7), (2,7), (5,7), (6,7)])
G20 = Graph( [(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2), (2,4), (1,7), (3,7), (4,7), (2,7), (5,7), (6,7)])
G21 = Graph([(1,2), (2,3), (3,4), (4,1), (1,7), (1,6), (1,5), (5,6), (6,7), (2,5), (2,6), (2,4), (3,6)])
G22 = Graph([(1,2), (1,3), (1,4), (2,3), (3,4), (4,2), (5,3), (5,2), (3,6), (2,7), (6,4), (4,7)])
G23 = Graph([(1,2), (1,3), (1,4), (2,3), (3,4), (4,2), (5,3), (5,2), (3,6), (2,7), (6,4), (4,7), (1,5), (1,6), (1,7)])
G24 = Graph([(1,3), (2,3), (3,4), (4,2), (5,3), (5,2), (3,6), (2,7), (6,4), (4,7), (1,5), (1,6), (1,7)])
G25 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (2,7), (3,5), (4,6), (5,6), (5,7), (6,7)])
G26 = Graph([(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (3,4), (4,5), (5,6), (6,2)]) #G26 is the only disconnected graph in the list.
G26.add_vertex(7)
non_wr_graphs_7_vertices = [G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20, G21, G22, G23, G24, G25, G26] 
#The graphs to be tested are the graphs in the list 'non_wr_graphs_7_vertices'.

graphs_with_no_6_vertex_wr_subgraph =[] #list for storing graphs that do not have a 6-vertex word-representable induced subgraph.
vertices= [1,2,3,4,5,6,7]
wr_subgraphs_6_vertex_count_list=[] #This list will store the number of 6-vertex word-representable induced subgraphs present in every graph examined.
all_6_subsets = list(combinations(vertices, 6)) #all possible 7-vertex subsets of list 'vertices'.

#Testing phase
for G in non_wr_graphs_7_vertices:
    is_bad = True  #indicates that the 7-vertex graph G under consideration has no word-representable 6-vertex I.S.
    wr_subgraph_6_vertex_count=0 #will count the number of 6-vertex word-representable induced subgraphs in graph G. 
    for t in all_6_subsets:
        H = G.subgraph(t) #induced subgraph of G on 7-vertex set 't'.
        if H.is_isomorphic(Non_wr_6_vertex_graph):
            continue
        else:
            is_bad = False #indicating the presence of a 6-vertex word-representable induced subgraph.
            wr_subgraph_6_vertex_count+=1
    wr_subgraphs_6_vertex_count_list.append(wr_subgraph_6_vertex_count)
    if is_bad:
        graphs_with_no_6_vertex_wr_subgraph.append(G)
print("Lowest value in the 'wr_subgraphs_6_vertex_count_list' list", min(wr_subgraphs_6_vertex_count_list))
#Every 7-vertex graph have at least min(wr_subgraphs_6_vertex_count_list) number of 6-vertex word-representable induced subgraphs.