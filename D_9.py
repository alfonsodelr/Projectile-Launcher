import pygame, sys

from pygame.constants import K_LEFT, K_RIGHT, KEYDOWN, KEYUP, QUIT

clock = pygame.time.Clock()

pygame.init()

WINDOW_SIZE = (800,600)

pygame.display.set_caption('MY GAME')

display = pygame.display.set_mode(WINDOW_SIZE)

player_image = pygame.image.load('image.png')

moving_left = False
moving_right = False

player_location = [50,50]

while True:

    display.fill((146,244,255))
    display.blit(player_image, player_location)
    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update()
    clock.tick(60)