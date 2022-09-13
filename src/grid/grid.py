import pygame
from pygame.locals import *
from time import sleep

from src.grid.square import Square

class Grid:
    def __init__(self, grid_size, square_size):
        self._start_color = (2, 230, 199)
        self._end_color = (0, 104, 243)
        self._square_size = square_size
        self._grid_size = grid_size

        self.grid = []
        for i in range(self._grid_size):
            self.grid.append([])
            for j in range(self._grid_size):
                self.grid[len(self.grid)-1].append(Square((i*self._square_size), (j*self._square_size), size=self._square_size))
    
    def get_color(self, x, y):
        if self.grid[x][y] is not None:
            return self.grid[x][y].color
        else:
            return None

    def override_color(self, x, y, new_color):
        if self.grid[x][y] is not None:
            self.grid[x][y].override_color(new_color)

    def select_square(self, x, y):
        if self.grid[x][y] is not None:
            self.grid[x][y].select()
    
    def mark_square(self, x, y):
        if self.grid[x][y] is not None:
            self.grid[x][y].mark()
    
    def mark_path(self, path):
        for s in path:
            x, y = s.split("-")
            self.mark_square(int(x), int(y))
            sleep(0.005)
    
    def set_start_square(self, x, y):
        if self.grid[x][y] is not None:
            self.grid[x][y].override_color(self._start_color)

    def set_end_square(self, x, y):
        if self.grid[x][y] is not None:
            self.grid[x][y].override_color(self._end_color)
    
    def delete_square(self, x, y):
        self.grid[x][y] = None
    
    def square_exists(self, x, y):
        if self.grid[x][y] is not None:
            return True
        else:
            return False

    def draw(self, surface):
        surface.fill((0, 0, 0))
        for i in range(self._grid_size):
            for j in range(self._grid_size):
                if self.grid[i][j] is not None:
                    self.grid[i][j].draw(surface)
    
    def __str__(self):
        result = ""
        for l in self.grid:
            result += str(l)
            result += "\n"
        return result
    
    def __len__(self):
        return len(self.grid)