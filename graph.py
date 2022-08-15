#Graph using Python

from re import T


class Graph:
    def __init__(self):
        self.adj_lst = {}
    
    def print_graph(self):
        for vertex in self.adj_lst:
            print(vertex, ':', self.adj_lst[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_lst.keys():
            self.adj_lst[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_lst.keys() and v2 in self.adj_lst.keys():
            self.adj_lst[v1].append(v2)
            self.adj_lst[v2].append(v1)
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_lst.keys() and v2 in self.adj_lst.keys():
            try:
                self.adj_lst[v1].remove(v2)
                self.adj_lst[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_lst.keys():
            #iterate over list of edges to remove it and then delete vertex
            for other_vertex in self.adj_lst[vertex]:
                self.adj_lst[other_vertex].remove(vertex)
            del self.adj_lst[vertex]
            return True
        return False


new_graph = Graph()
new_graph.add_vertex('X')
new_graph.print_graph()
new_graph.add_vertex(1)
new_graph.add_vertex(2)
new_graph.add_edge(1, 2)
new_graph.print_graph()
# new_graph.remove_edge(1, 2)
# new_graph.print_graph()
new_graph.remove_vertex(1)
new_graph.print_graph()
