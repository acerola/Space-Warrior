import pygame
import sys
import math
from pygame.locals import *

SCROLLSPEED = 10
BULLET_MAX = 100

img_background = pygame.image.load("image/background3.png")
img_ship = [
    pygame.image.load("image/playerShip1_blue.png"),
    pygame.image.load("image/playerShip2_blue.png"),
    pygame.image.load("image/shipFire.png"),
]

img_weapon = pygame.image.load("image/lasers/laserRed16.png")


timer = 0
background_ypos = 0

player_x = 512
player_y = 960
player_d = 0

key_space = 0
key_z = 0

bullet_no = 0
bullet_f = [False] * BULLET_MAX
bullet_x = [0] * BULLET_MAX
bullet_y = [0] * BULLET_MAX
bullet_a = [0] * BULLET_MAX

def set_bullet(typ):
    global bullet_no
    if typ == 0:
        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 270
        bullet_no = (bullet_no + 1 )%BULLET_MAX

    if typ == 10:
        for i in range(0,370,10):
            bullet_f[bullet_no] = True
            bullet_x[bullet_no] = player_x
            bullet_y[bullet_no] = player_y - 30
            bullet_a[bullet_no] = i
            bullet_no = (bullet_no + 1) % BULLET_MAX


def move_bullet(screen):
    for i in range(BULLET_MAX):
        if bullet_f[i] == True:
            bullet_x[i] = bullet_x[i] + 36 * math.cos(math.radians((bullet_a[i])))
            bullet_y[i] = bullet_y[i] + 36 * math.sin(math.radians((bullet_a[i])))
            img_rz = pygame.transform.rotozoom(img_weapon , -90 - bullet_a[i] , 1.0)
            screen.blit(img_rz, [bullet_x[i] - img_rz.get_width() / 2 , bullet_y[i] - img_rz.get_height() / 2])
            if bullet_y[i] < 0 or bullet_x[i] < 0 or bullet_x[i] > 960:
                bullet_f[i] = False


def move_ship(screen, key):
    global player_x,player_y,player_d,key_space,key_z
    player_d = 0
    if key[K_UP] == 1:
        player_d = 1
        player_y = player_y - 20
        if player_y < 80:
            player_y = 80

    if key[K_DOWN] == 1:
        player_d = 1
        player_y = player_y + 20
        if player_y > 960:
            player_y = 960

    if key[K_LEFT] == 1:
        player_d = 1
        player_x = player_x - 20
        if player_x < 80:
            player_x = 80

    if key[K_RIGHT] == 1:
        player_d = 1
        player_x = player_x + 20
        if player_x > 920:
            player_x = 920
    key_space = (key_space + 1) * key[K_SPACE]
    if key_space % 5 == 1:
        set_bullet(0)
    key_z = (key_z + 1) * key[K_z]
    if key_z == 1:
        set_bullet(10)
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
        move_bullet(screen)

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
