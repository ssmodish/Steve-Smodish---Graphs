"""
Simple graph implementation
"""

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


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)



class Graph():
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Create an empty list (set) of visited vertices
        visited = set()
        # put start vertex in our queue
        q.enqueue(starting_vertex_id)
        # while queue is not empty
        while q.size() > 0:
            # dequeue the first node
            v = q.dequeue()
            # if that node hasn't been visited
            if v not in visited:
                # mark it as visited
                print(v)
                visited.add(v)
                # then put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        # create an empty stack
        s = Stack()
        # create an empty set of visited vertices
        visited = set()
        # put the starting vertex on the stack
        s.push(starting_vertex_id)
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex off the stack
            v = s.pop()
            # if that node has not been visited
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # then put all of it's children into the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)



## Part 3.5: Implement Depth-First Traversal using Recursion
    # visited =
    def recursive_dft(self, starting_vertex):
        visited = set()
        # def recursive-traverse(self, vertex)
        def recursive_traverse(vertex):
            # if not visited
            if vertex not in visited:
                # add to visited
                visited.add(vertex)
                # print
                print(vertex)
                # for neighbor in self.vertices[]:
                for neighbor in self.vertices[vertex]:
                    # recursive-traverse(neighbor)
                    recursive_traverse(neighbor)

        # recursive-traverse (starting vertex)
        recursive_traverse(starting_vertex)


## Part 4: Implement Breadth-First Search
    def bfs(self, starting_vertex, target):
    # queue
        q = Queue()
    # visited
        visited = set()
    # enqueue start as a list
        q.enqueue([starting_vertex])
    # while q
        while q.size() > 0:
        # dequeue list
            path = q.dequeue()
        # if last item in list is not visited,
            v = path[-1]
            if v not in visited:
            # mark as visited
                visited.add(v)
            # does last item in the list match target?
                if v == target:
                # return path
                    return path

            # add lists including neighbors to queue
                for neighbor in self.vertices[v]:
                # copy the current path
                    new_path = list(path)
                # add neighbors to that path
                    new_path.append(neighbor)
                # put those paths in the queue
                    q.enqueue(new_path)



## Part 5: Implement Depth-First Search
    def dfs(self, starting_vertex, target):
    # stack
        s = Stack()
    # visited
        visited = set()
    # push start as a list
        s.push([starting_vertex])
    # while s
        while s.size() > 0:
        # pop list
            path = s.pop()
        # if last item in list is not visited,
            v = path[-1]
            if v not in visited:
            # mark as visited
                visited.add(v)
            # does last item in the list match target?
                if v == target:
                # return path
                    return path

            # add lists including neighbors to stack
                for neighbor in self.vertices[v]:
                # copy the current path
                    new_path = list(path)
                # add neighbors to that path
                    new_path.append(neighbor)
                # put those paths in the stack
                    s.push(new_path)






