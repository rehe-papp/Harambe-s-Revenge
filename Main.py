import pygame
from random import randint
import sys
import time

pygame.init ()

#põhiväärtused

screen = pygame.display.set_mode ([1000, 500])

length = 50

tropp_y = 400

speed_y = 0

tropp_dir = 1

score = 0

def quit():
    pygame.quit()

game_start = False
    

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                game_start = True
                tropp_dir = 3

            elif event.key == pygame.K_RIGHT:
                game_start = True
                tropp_dir = 1

            elif event.key == pygame.K_SPACE:
                game_start = True
                speed_y = -50

    if game_start:

        screen.fill ([0, 225, 0], [0, 450, 1000, 50])
        screen.fill ([0, 100, 225], [0, 0, 1000, 450])

        tropp = pygame.Rect ([100, tropp_y, length, length])
        pygame.draw.rect (screen, [100, 100, 100], tropp)

        speed_y += 5
        tropp_y += speed_y
            
        
        if tropp_y == 400:
            speed_y = -5




























        pygame.display.flip()
        pygame.time.wait(60)
