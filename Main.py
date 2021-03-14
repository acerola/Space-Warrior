import pygame
import sys
from pygame.locals import *

SCROLLSPEED = 10

img_background = pygame.image.load("image/background3.png")
img_ship = [
    pygame.image.load("image/playerShip1_blue.png"),
    pygame.image.load("image/playerShip2_blue.png"),
    pygame.image.load("image/shipFire.png"),
]

timer = 0
background_ypos = 0

player_x = 512
player_y = 960
player_d = 0

def move_ship(screen, key):
    global player_x,player_y,player_d
    player_d = 0
    if key[pygame.K_UP] == 1:
        player_y = player_y - 20
        if player_y < 80:
            player_y = 80

    if key[pygame.K_DOWN] == 1:
        player_y = player_y + 20
        if player_y > 960:
            player_y = 960

    if key[pygame.K_LEFT] == 1:
        player_d = 1
        player_x = player_x - 20
        if player_x < 80:
            player_x = 80

    if key[pygame.K_RIGHT] == 1:
        player_d = 1
        player_x = player_x + 20
        if player_x > 920:
            player_x = 920
    screen.blit(img_ship[2], [player_x - 8, player_y + 40 + (timer % 4) * 2])
    screen.blit(img_ship[player_d] , [player_x - 49, player_y - 37])


def main():
    global timer , background_ypos
    pygame.init()
    pygame.display.set_caption("Space Warrior")
    screen = pygame.display.set_mode((1024,1024))

    clock = pygame.time.Clock()


    while True:
        timer = timer + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        background_ypos = (background_ypos + SCROLLSPEED) % 1024
        screen.blit(img_background, [0,background_ypos - 1024])
        screen.blit(img_background, [0,background_ypos])

        key = pygame.key.get_pressed()
        move_ship(screen,key)


        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
