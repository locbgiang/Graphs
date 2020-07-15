'''
def bfs(self, starting_vertex_id, target_vertex_id):
    q = Queue()                          # create a queue
    q.enqueue([starting_vertex_id])       # store the first queue as [starting_vertext_id]

    visited = set()                      # keep track of visited

    while q.size() > 0:                  # while q side is greater than 0
        path = q.dequeue()               # path is created from the queue
        v = path[-1]                     # last number on path is v
        if v not in visited:             # if v is not in visited
            if v == target_vertex_id:       # if v is target vertex 
                return path                 # return the current path
            visited.add(v)       # if v is not target add it to visited
            for next_vert in self.get_neighbors(v):     # logic for the next vertex
                new_path = list(path)                # new path is created from copying current path
                new_path.append(next_vert)           # append the latest vertex
                q.enqueue(new_path)                 # enqueue the new path
'''
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def find_ladders(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                for neighbors in get_neighbors(v):
                    path_copy = list(path)
                    path_copy.append(neighbors)
                    q.enqueue(path_copy)
    return None