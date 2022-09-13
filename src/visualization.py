import pygame
from pygame.locals import *
from threading import Thread
import sys

from src.grid.grid import Grid
from src.data_structures.graph import Graph
from src.algorithms import *


class Visualization:
    def __init__(self, options: dict):
        print("Loading visualization...")
        options_keys = options.keys()

        # Set defaults
        if "screen_size" not in options_keys:
            options["screen_size"] = 1000                               # Default screen size
        if "algorithm" not in options_keys:
            raise RuntimeError("An algorithm must be selected")         # Algorithm required
        if "start" not in options_keys:
            raise RuntimeError("A start point must be selected")        # Start point required
        if "end" not in options_keys:
            raise RuntimeError("An end point must be selected")         # End point required
        if "background_color" not in options_keys:
            options["background_color"] = (255, 255, 255)               # Default background color
        if "square_color" not in options_keys:
            options["square_color"] = (0, 130, 24)                      # Default square color
        if "square_size" not in options_keys:
            options["square_size"] = 20                                 # Default square size
        if "grid_size" not in options_keys:
            options["grid_size"] = 50                                   # Default grid size

        # Pygame
        self._running = True
        self._display_surface = None
        self.size = self.width, self.height = options["screen_size"], options["screen_size"]
        self._deleting = False

        # Algorithm
        self._algorithm = options["algorithm"]
        self._start = options["start"]
        self._end = options["end"]

        self._executing_algorithm = False
        self.weighted_algorithms = [uniform_cost, a_star, limited_a_star]

        # Colors (currently useless)
        self._background_color = options["background_color"]
        self._square_color = options["square_color"]

        # Grid
        self._square_size = options["square_size"]
        self._grid_size = options["grid_size"]
        
        self.grid = Grid(self._grid_size, self._square_size)
        start_x, start_y = self._start
        self.grid.set_start_square(start_x, start_y)
        end_x, end_y = self._end
        self.grid.set_end_square(end_x, end_y)        
    
    def on_init(self):
        pygame.init()
        self._display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_SPACE:
                if not self._executing_algorithm:
                    # Init graph
                    self.graph = Graph()
                    self.graph.recreate_grid(grid=self.grid, add_weight=self._algorithm in self.weighted_algorithms)
                    # Run algorithm in different thread
                    thread = Thread(target=self._algorithm, args=(self.graph, self._start, self._end, self.grid))
                    thread.start()
                    self._executing_algorithm = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self._deleting = True
            elif event.button == 2:
                pos = mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_pos = grid_x, grid_y = (int(mouse_x/self._square_size), int(mouse_y/self._square_size))
                print(grid_pos)
            elif event.button == 3:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self._deleting = False
    
    def on_loop(self):
        if self._deleting:
            pos = mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_pos = grid_x, grid_y = (int(mouse_x/self._square_size), int(mouse_y/self._square_size))
            self.grid.delete_square(grid_x, grid_y)

    def on_render(self):
        pygame.display.flip()
        self.grid.draw(self._display_surface)

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()