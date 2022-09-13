import pygame
from pygame.locals import *


class Square:
    def __init__(self, x, y, size, padding=2):
        self._default_color = (39, 55, 72)
        self._selected_color = (23, 140, 89)
        self._mark_color = (255, 255, 0)

        self.x = x
        self.y = y
        self.color = self._default_color
        self.padding = padding
        self.size = size
        self.center_pos = (self.x + (self.size/2), self.y + (self.size/2))
        self.color_overridden = False
        self.selected = False
        self.marked = False
    
    def get_color(self):
        if self.color_overridden:
            return self.color
        else:
            if self.selected:
                return self._selected_color
            else:
                return self._default_color
    
    def override_color(self, new_color):
        self.color_overridden = True
        self.color = new_color
    
    def select(self):
        self.selected = True
    
    def unselect(self):
        self.selected = False
    
    def mark(self):
        self.marked = True

    def unmark(self):
        self.marked = False
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.get_color(), pygame.Rect((self.x+self.padding), (self.y+self.padding), (self.size-(2*self.padding)), (self.size-(2*self.padding))))
        if self.marked:
            pygame.draw.circle(surface, self._mark_color, self.center_pos, 4)