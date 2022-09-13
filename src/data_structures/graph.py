import math
from random import randrange
import networkx as nx
import matplotlib.pyplot as plt

from src.grid.grid import Grid


class Node:
    def __init__(self, label):
        self.label = label
        self.adjacents = []
        self.distance = math.inf
        self.prev = None

    def __str__(self):
        return str(self.label)

    def add_edge_to(self, v, weight):
        self.adjacents.append((v, weight))


class Graph:
    def __init__(self):
        self.vertices = []

    def __str__(self):
        string = ""
        for v in self.vertices:
            string += str(v.label) + ": ["
            for a in v.adjacents:
                string += str(a[0].label) + ", "
            string = string.removesuffix(", ")
            string += "]\n"
        return string

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def __getitem__(self, n):
        return self.vertices[n]

    def add_vertice(self, label):
        self.vertices.append(Node(label))

    def get_vertice_reference(self, v):
        for vertice in self.vertices:
            if vertice.label == v:
                return vertice

    def add_edge(self, a, b, weight=None):
        v_from = self.get_vertice_reference(a)
        if v_from is None:
            self.add_vertice(a)
            v_from = self.get_vertice_reference(a)
        v_to = self.get_vertice_reference(b)
        if v_to is None:
            self.add_vertice(b)
            v_to = self.get_vertice_reference(b)
        v_from.add_edge_to(v_to, weight)

    def verify_edge(self, a, b):
        a_pointer = self.get_vertice_reference(a)
        for v, w in a_pointer.adjacents:
            if v.label == b:
                return True
        return False

    def get_adjacents(self, v):
        return self.get_vertice_reference(v).adjacents

    def get_weight(self, v, w):
        for a in self.get_vertice_reference(v).adjacents:
            if a[0].label == w:
                return a[1]
        return None
    
    def recreate_grid(self, grid: Grid, add_weight: bool):
        grid_size = len(grid)
        for i in range(grid_size):
            for j in range(grid_size):
                self.add_vertice(f"{i}-{j}")
        for i in range(grid_size):
            for j in range(grid_size):
                if grid.square_exists(i, j):
                    # Up
                    if i != 0:
                        self.add_edge(f"{i}-{j}", f"{i-1}-{j}", weight=(randrange(10) if add_weight else None))
                    # Down
                    if i != grid_size-1:
                        self.add_edge(f"{i}-{j}", f"{i+1}-{j}", weight=(randrange(10) if add_weight else None))
                    # Left
                    if j != 0:
                        self.add_edge(f"{i}-{j}", f"{i}-{j-1}", weight=(randrange(10) if add_weight else None))
                    # Right
                    if j != grid_size-1:
                        self.add_edge(f"{i}-{j}", f"{i}-{j+1}", weight=(randrange(10) if add_weight else None))

                    # Up-Left
                    if i != 0 and j != 0:
                        self.add_edge(f"{i}-{j}", f"{i-1}-{j-1}", weight=(randrange(10) if add_weight else None))
                    # Up-Right
                    if i != 0 and j != grid_size-1:
                        self.add_edge(f"{i}-{j}", f"{i-1}-{j+1}", weight=(randrange(10) if add_weight else None))
                    # Down-Left
                    if i != grid_size-1 and j != 0:
                        self.add_edge(f"{i}-{j}", f"{i+1}-{j-1}", weight=(randrange(10) if add_weight else None))
                    # Down-Right
                    if i != grid_size-1 and j != grid_size-1:
                        self.add_edge(f"{i}-{j}", f"{i+1}-{j+1}", weight=(randrange(10) if add_weight else None))

    def visualize(self):
        edges = []
        for a in self:
            for e in a.adjacents:
                edges.append([a.label, e[0]])
        g = nx()
        g.add_edges_from(edges)
        nx.draw_networkx(g)
        plt.show()