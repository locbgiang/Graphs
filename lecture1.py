class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('nonexistent vert')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertext_id):
        # create an empty queue
        # create a set to store the visited nodes
        q = Queue()
        visited = set()
        # init: enqueue the starting node
        q.enqueue(starting_vertext_id)
        # while the queue isnt empty
        while q.size() > 0:
            # dequeue the first item
            v = q.dequeue()
            # if it's not be visited:
            if v not in visited:
                visited.add(v)
                print(f'visted {v}')
                # mark as visited (ie add to the visited list)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
                # add all neighbors to the queue



g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')


g.add_edge('A', 'B')
g.add_edge('A', 'C')

g.add_edge('B', 'A')
g.add_edge('B', 'B')
g.add_edge('B', 'C')

g.add_edge('C', 'D')

g.add_edge('D', 'C')

g.bft('B')

#print(g.get_neighbors('C'))