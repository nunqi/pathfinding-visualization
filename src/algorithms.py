from time import sleep
import math

from src.grid.grid import Grid
from src.data_structures.graph import Graph
from src.data_structures.tree import Tree


def bfs(graph: Graph, start: tuple, end: tuple, grid: Grid) -> None:
    start_str = f"{start[0]}-{start[1]}"
    end_str = f"{end[0]}-{end[1]}"

    path_tree = Tree(start_str)
    queue = [start_str]
    explored = [start_str]
    while queue:
        v = queue.pop(0)

        x, y = v.split("-")
        grid.select_square(int(x), int(y))
        sleep(0.005)

        for w_reference,_ in graph.get_adjacents(v):
            w = w_reference.label
            if w not in explored:
                explored.append(w)
                path_tree.add(w, v)
                queue.append(w)

        if v == end_str:
            break
    
    grid.mark_path(path_tree.path(end_str))
    
def dfs(graph: Graph, start: tuple, end: tuple, grid: Grid) -> None:
    start_str = f"{start[0]}-{start[1]}"
    end_str = f"{end[0]}-{end[1]}"

    path_tree = Tree(start_str)
    stack = [start_str]
    explored = [start_str]
    while stack:
        v = stack.pop()

        x, y = v.split("-")
        grid.select_square(int(x), int(y))
        sleep(0.005)

        for w_reference,_ in graph.get_adjacents(v):
            w = w_reference.label
            if w not in explored:
                explored.append(w)
                path_tree.add(w, v)
                stack.append(w)

        if v == end_str:
            break
    
    grid.mark_path(path_tree.path(end_str))

def uniform_cost(graph: Graph, start: tuple, end: tuple, grid: Grid) -> None:
    start_str = f"{start[0]}-{start[1]}"
    end_str = f"{end[0]}-{end[1]}"

    path_tree = Tree(start_str)
    priority_queue = [(start_str, 0)]
    explored = [start_str]
    while priority_queue:
        priority_queue.sort(key=lambda x: x[1])
        v, v_weight = priority_queue.pop(0)

        x, y = v.split("-")
        grid.select_square(int(x), int(y))
        sleep(0.005)

        for w_reference,w_weight in graph.get_adjacents(v):
            w = w_reference.label
            if w not in explored:
                explored.append(w)
                path_tree.add(w, v)
                priority_queue.append((w, w_weight + v_weight))

        if v == end_str:
            break
    
    grid.mark_path(path_tree.path(end_str))

def best_first(graph: Graph, start: tuple, end: tuple, grid: Grid) -> None:
    def heuristics(s, e):
        s_tuple = tuple(int(x) for x in s.split("-"))
        e_tuple = tuple(int(x) for x in e.split("-"))

        return math.dist(s_tuple, e_tuple)
    
    start_str = f"{start[0]}-{start[1]}"
    end_str = f"{end[0]}-{end[1]}"

    path_tree = Tree(start_str)
    priority_queue = [(start_str, 0)]
    explored = [start_str]
    while priority_queue:
        priority_queue.sort(key=lambda x: x[1])
        v,_ = priority_queue.pop(0)

        x, y = v.split("-")
        grid.select_square(int(x), int(y))
        sleep(0.005)

        for w_reference,_ in graph.get_adjacents(v):
            w = w_reference.label
            if w not in explored:
                explored.append(w)
                path_tree.add(w, v)
                priority_queue.append((w, heuristics(w, end_str)))

        if v == end_str:
            break
    
    grid.mark_path(path_tree.path(end_str))

def hill_climbing(graph: Graph, start: tuple, end: tuple, grid: Grid) -> None:
    def distance(s, e):
        s_tuple = tuple(int(x) for x in s.split("-"))
        e_tuple = tuple(int(x) for x in e.split("-"))

        return math.dist(s_tuple, e_tuple)

    start_str = f"{start[0]}-{start[1]}"
    end_str = f"{end[0]}-{end[1]}"
    
    path = [start_str]
    current_square = start_str
    tallest_adjacent = current_square
    while tallest_adjacent is not None:
        tallest_adjacent = None
        tallest_adjacent_height = -1

        x, y = current_square.split("-")
        grid.select_square(int(x), int(y))
        sleep(0.005)

        for w_reference,_ in graph.get_adjacents(current_square):
            w = w_reference.label
            if distance(w, end_str) > tallest_adjacent_height:
                tallest_adjacent = w
        path.append(current_square)
        current_square = tallest_adjacent
    
    if current_square != end_str:
        print("Local maximum reached")
    else:
        print("Global maximum reached")

    grid.mark_path(path)

def a_star(graph: Graph, start: tuple, end: tuple, grid: Grid) -> None:
    def heuristics(s, e):
        s_tuple = tuple(int(x) for x in s.split("-"))
        e_tuple = tuple(int(x) for x in e.split("-"))

        return math.dist(s_tuple, e_tuple)
    
    start_str = f"{start[0]}-{start[1]}"
    end_str = f"{end[0]}-{end[1]}"

    path_tree = Tree(start_str)
    priority_queue = [(start_str, 0)]
    explored = [start_str]
    while priority_queue:
        priority_queue.sort(key=lambda x: x[1])
        v, v_weight = priority_queue.pop(0)

        x, y = v.split("-")
        grid.select_square(int(x), int(y))
        sleep(0.005)

        for w_reference,w_weight in graph.get_adjacents(v):
            w = w_reference.label
            if w not in explored:
                explored.append(w)
                path_tree.add(w, v)
                priority_queue.append((w, heuristics(w, end_str) + w_weight))

        if v == end_str:
            break
    
    grid.mark_path(path_tree.path(end_str))

def limited_a_star(graph: Graph, start: tuple, end: tuple, grid: Grid) -> None:
    pass