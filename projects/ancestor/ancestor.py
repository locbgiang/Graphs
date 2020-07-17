from graph import Graph
def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for a in ancestors:                  # Graphing the ancestors
        g.add_vertex(a[0])               
        g.add_vertex(a[1])
    for a in ancestors:                  # add edge
        g.add_edge(a[1],a[0])

    parents = g.dft(starting_node)        
    if len(parents) == 1:                   # if starting node has no ancestor
        return -1                       # return 1

    paths = []               
    for end in parents:                                 # find all path from starting node
        paths.append(g.dfs(starting_node, end))


    longestpath = 0
    longestlength = 0
    for i in range(len(paths)):                     # find longest path
        if len(paths[i]) > longestlength:
            longestpath = paths[i]
            longestlength = len(paths[i])
    return longestpath[-1]                             # return the final node from longest



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors,8)

'''
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_vertex(8)
graph.add_vertex(9)
graph.add_vertex(10)
graph.add_vertex(11)

graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(10, 1)
graph.add_edge(4, 5)
graph.add_edge(4, 8)
graph.add_edge(11, 8)
graph.add_edge(3, 6)
graph.add_edge(5, 6)
graph.add_edge(5, 7)
graph.add_edge(8, 9)


earliest_ancestor(10, 6)
'''