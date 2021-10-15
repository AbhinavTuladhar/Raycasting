import pygame
import math
import numpy as np
from Boundary import Boundary
from Ray import Ray
from Source import Source
from Constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ray Casting")

rays = []
walls = []

# Create random boundaries
for _ in range(NUMBER_OF_WALLS):
    x1 = np.random.randint(0, WIDTH)
    y1 = np.random.randint(0, HEIGHT)
    x2 = np.random.randint(0, WIDTH)
    y2 = np.random.randint(0, HEIGHT)
    temp = Boundary(screen, x1, y1, x2, y2)
    walls.append(temp)

# Four boundaries surrounding the screen
walls.append(Boundary(screen, 0, 0, WIDTH, 0))
walls.append(Boundary(screen, 0, 0, 0, HEIGHT))
walls.append(Boundary(screen, 0, HEIGHT - 2, WIDTH, HEIGHT - 2))
walls.append(Boundary(screen, WIDTH, 0, WIDTH, HEIGHT - 2))

# Create the light source
source = Source(screen)

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    mx, my = pygame.mouse.get_pos()

    # Show all boundaries
    for wall in walls:
        wall.show()

    source.update(mx, my)   # Make the light source follow the cursor
    source.show()
    source.look(walls)
    
    # ray.lookAt(mx, my)
    # pt = ray.cast(wall)
    # if pt:
    #     pygame.draw.circle(screen, WHITE, (pt.x, pt.y), 4)
    pygame.display.update()
pygame.quit()