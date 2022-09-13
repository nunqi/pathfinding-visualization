from sys import argv
from inspect import getmembers, isfunction

from src.visualization import Visualization
from src import algorithms
from src.algorithms import *


"""
Implemented algorithms:
    - BFS (bfs)
    - DFS (dfs)
    - Uniform-cost search (uniform_cost)
    - Best-first search (best_first)
    - Hill Climbing (hill_climbing) [INCOMPLETE]
    - A* (a_star)
    - A* variation with limited memory and recursivity (limited_a_star) [TODO]
"""


if __name__ == "__main__" :    
    algorithm = argv[1]
    start = int(argv[2]), int(argv[3])
    end = int(argv[4]), int(argv[5])

    if algorithm in [a[0] for a in getmembers(algorithms, isfunction)]:
        options = {
            "algorithm": locals()[algorithm],
            "start": start,
            "end": end,
            "screen_size": 800,                     # optional
            "grid_size": 50,                        # optional
            "square_size": 16                       # optional
        }
        visualization = Visualization(options=options)
        visualization.on_execute()
    else:
        print("Invalid algorithm name")