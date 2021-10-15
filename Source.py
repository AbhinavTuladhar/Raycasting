import pygame
from Boundary import Boundary
from Ray import Ray
from Vector import Vector
import numpy as np
import math
from Constants import *

def distance(V1, V2):
    return np.sqrt(np.sum((V2.x - V1.x) ** 2 + (V2.y - V1.y) ** 2))

class Source:
    def __init__(self, screen):
        self.screen = screen
        self.pos = Vector(500, 500)     # Arbitrary parameters

    def update(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def show(self):
        self.rays = []                  # Store all the ray emerging from the source
        for x in range(0, 361, 360 // NUMBER_OF_RAYS):
            temp = Ray(self.screen, self.pos.x, self.pos.y, np.radians(x))
            self.rays.append(temp)
        for ray in self.rays:
            ray.show()

    def look(self, walls):
        for ray in self.rays:
            closest = None
            record = math.inf                   # Assume that the nearest boundary is at infinity
            for wall in walls:
                pt = ray.cast(wall)             # Obtain the intersection point
                if pt:              
                    d = distance(self.pos, pt)  # Find the distance between the source and the intersection point
                    if d < record:              # If it is smaller than the currently smallest distance,
                        record = d              # update the respective values
                        closest = pt            # Vector containing the nearest intersection point
            if closest:                     
                # Draw the light ray up to the nearest boundary
                pygame.draw.line(self.screen, WHITE, (self.pos.x, self.pos.y), (closest.x, closest.y))