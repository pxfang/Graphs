#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph


def main(num_vertices=8, num_edges=8):
    """Build and show random graph."""
    graph = Graph()
    # Add appropriate number of vertices
    for num in range(num_vertices):
        graph.add_vertex(str(num))

    # Add random edges between vertices
    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        # TODO check if edge already exists
        graph.add_edge(vertices[0], vertices[1])

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()


if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()  # accept defaults

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex, edges=()):
        if not set(edges).issubset(self,vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        self.vertices(vertex) = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

        def search(self, start, target=None, method='dfs'):
            firstsearch = [start]
            pop_index = 0 if method == 'bfs' else -1
            visited = set()

            while firstsearch:
                current = firstsearch.pop(pop_index)
                if current == target:
                    break
                visited.add(current)
                firstsearch.extend(self.vertices[current] = visited)
            
            return visited

