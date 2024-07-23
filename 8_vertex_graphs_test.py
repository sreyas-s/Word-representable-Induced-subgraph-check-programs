import copy
from sage.graphs.graph import Graph
from sage.sets.set import Set
from itertools import combinations

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
non_wr_graphs_7_vertices = [G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20, G21, G22, G23, G24, G25, G26]  # Add more graphs as needed, G3, G4, ..., G26
#stored all non-word-representable graphs on 7 vertices to the database 'non_wr_graphs_7_vertices'. (Storing phase -done).

#Next is the Generation phase of all 8-vertex graphs to be tested. (We add an eighth vertex and look at all possible graphs generated).

#Helper function to generate subsets of a set.
def generate_subsets(nums):
    subsets = [[]]  # Start with an empty subset
    def backtrack(start, curr_subset):
        if start == len(nums):
            return
        for i in range(start, len(nums)):
            curr_subset.append(nums[i])
            subsets.append(curr_subset[:])  
            backtrack(i + 1, curr_subset)
            curr_subset.pop()
    backtrack(0, [])
    return subsets

edge_list = [(1,8), (2,8), (3,8), (4,8), (5,8), (6,8), (7,8)] #all possible edges when 8th vertex is added.
subsets_edges = generate_subsets(edge_list) #'subsets_edges' is a list containing all possible subsets of 'edge_list'.
all_8_vertex_graphs_to_be_tested = []
for i in range(26):
    for j in subsets_edges:
        G = copy.deepcopy(non_wr_graphs_7_vertices[i])
        G.add_vertex(8)
        G.add_edges(j)
        all_8_vertex_graphs_to_be_tested.append(G)
#Generation phase -Done. All the 8-vertex graphs to be tested are stored in the list 'all_8_vertex_graphs_to_be_tested'.
graphs_with_no_7_vertex_wr_subgraph =[] #list for storing graphs that do not have a 7-vertex word-representable induced subgraph.
graphs_having_7_vertex_wr_subgraph_count=0 #will store the count of 8 vertex graphs that have 7-vertex word-representable induced subgraph in it.
vertices= [1,2,3,4,5,6,7,8]
all_7_subsets = list(combinations(vertices, 7))
#Testing phase
for G in all_8_vertex_graphs_to_be_tested:
    is_bad = True  #indicates that the 8-vertex graph G under consideration has no word-representable 7-vertex I.S.
    for t in all_7_subsets:
        H = G.subgraph(t) #induced subgraph of G on 7-vertex set 't'.
        count = 0
        for J in non_wr_graphs_7_vertices:
            if H.is_isomorphic(J):
                count += 1
            else:
                continue
        if count == 0: #If we get a subgraph H in G which is not isomorphic to any of the 7-vertex non-word-representable graphs.
            is_bad = False #indicating the presence of a 7-vertex word-representable induced subgraph.
    if is_bad:
        graphs_with_no_7_vertex_wr_subgraph.append(G) #If 'is_bad' is True, it means that 'count' is greater than 0 for all 7-vertex subgraphs.
    else:
        graphs_having_7_vertex_wr_subgraph_count += 1
#'graphs_with_no_7_vertex_wr_subgraph' list can contain isomorphic graphs in it, now we filter out the isomorphic ones from it.
non_isomorphic_graphs_with_no_7vertex_wr_subgraph = [] 
non_isomorphic_count = 0 
for graph1 in graphs_with_no_7_vertex_wr_subgraph:
    is_non_isomorphic=True
    for graph2 in non_isomorphic_graphs_with_no_7vertex_wr_subgraph:
        if graph1.is_isomorphic(graph2):
            is_non_isomorphic=False
            break
    if is_non_isomorphic:
        non_isomorphic_count += 1
        non_isomorphic_graphs_with_no_7vertex_wr_subgraph.append(graph1) 

print("Count of non-isomorphic graphs that do not have a 7-vertex word-representable I.S:", non_isomorphic_count)
#To enumerate the edge list of each graph that does not have a 7-vertex word-representable I.S
for i, graph in enumerate(non_isomorphic_graphs_with_no_7vertex_wr_subgraph):
    # Get the list of edges in the current graph
    edges = graph.edges()
    # Enumerate over the edges and print the index and the edge
    print(f"Edges in graph_{i}:")
    for j, edge in enumerate(edges):
        print(f"{j+1}. {edge}")
    print()  # Add a blank line for readability
