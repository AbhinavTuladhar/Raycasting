import pygame
from Vector import Vector
from Constants import *

class Boundary:
    def __init__(self, screen, x1, y1, x2, y2):
        self.screen = screen
        self.a = Vector(x1, y1)
        self.b = Vector(x2, y2)
        self.slope_x = self.b.x - self.a.x
        self.slope_y = self.b.y - self.a.y
    
    def show(self):
        pygame.draw.line(self.screen, WHITE,
            (self.a.x, self.a.y),
            (self.b.x, self.b.y),
            2
        )