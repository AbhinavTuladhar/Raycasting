from Vector import Vector
import pygame
import math
from Constants import *

class Ray:
    def __init__(self, screen, x, y, angle):
        self.screen = screen
        self.pos = Vector(x, y)
        self.dir = Vector(math.cos(angle), math.sin(angle))
    
    # Unecessary function
    # def lookAt(self, x, y):
    #     self.dir.x = x - self.pos.x
    #     self.dir.y = y - self.pos.y
    #     magnitude = lambda x, y : np.sqrt(x ** 2 + y ** 2)
    #     answer = magnitude(self.dir.x, self.dir.y)
    #     self.dir.x = self.dir.x / answer
    #     self.dir.y = self.dir.y / answer
    
    def show(self):
        pygame.draw.line(self.screen, WHITE,
            (self.pos.x, self.pos.y),
            (self.pos.x + self.dir.x * 10 , self.pos.y + self.dir.y * 10)
        )

    # Function to check line - line intersection.
    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        # If the denominator of checking function is zero, then the ray is
        # parallel to the boundary, so skip drawing it
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return
        
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        # If the condition is true, then the lines intersect.
        # Then return a vector containing the point of intersection.
        if t > 0 and t < 1 and u > 0:
            pt = Vector(0, 0)
            pt.x = x1 + t * (x2 - x1)
            pt.y = y1 + t * (y2 - y1)
            return pt
        else:
            return