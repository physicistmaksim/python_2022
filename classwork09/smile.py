import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((255, 255, 255))

circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 2)

circle(screen, (255, 0, 0), (240, 170), 20)
circle(screen, (0, 0, 0), (240, 170), 20, 2)
circle(screen, (0, 0, 0), (240, 170), 10)

circle(screen, (255, 0, 0), (160, 170), 20)
circle(screen, (0, 0, 0), (160, 170), 20, 2)
circle(screen, (0, 0, 0), (160, 170), 10)

rect(screen, (0, 0, 0), (150, 230, 100, 20))

polygon(screen, (0, 0, 0), [(210, 175), (250, 125), (300, 125)])

polygon(screen, (0, 0, 0), [(190, 175), (150, 125), (100, 125)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()