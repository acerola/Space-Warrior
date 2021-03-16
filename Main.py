import pygame
import sys
import math
import random
from pygame.locals import *


SCROLLSPEED = 10
BULLET_MAX = 100
ENEMY_MAX = 100
ENEMY_BULLET_MAX = 100

LINE_TOP = -80
LINE_BOTTOM = 1124
LINE_LEFT = -80
LINE_RIGHT = 1124



img_background = pygame.image.load("image/background3.png")
img_ship = [
    pygame.image.load("image/playerShip1_blue.png"),
    pygame.image.load("image/playerShip2_blue.png"),
    pygame.image.load("image/shipFire.png"),
]

img_player_weapon = [
    pygame.image.load("image/lasers/laserRed16.png"), # player laser 1

]

img_enemy_weapon = [
    pygame.image.load("image/lasers/laserBlue11.png") # enemy laser 1
]

img_enemy = [
    pygame.image.load("image/enemies/enemyBlack1.png")
]




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

enemy_no = 0
enemy_f = [False] * ENEMY_MAX
enemy_x = [0] * ENEMY_MAX
enemy_y = [0] * ENEMY_MAX
enemy_a = [0] * ENEMY_MAX
enemy_type = [0] * ENEMY_MAX
enemy_speed = [0] * ENEMY_MAX



enemy_bullet_no = 0
enemy_bullet_f = [False] * ENEMY_MAX
enemy_bullet_x = [0] * ENEMY_MAX
enemy_bullet_y = [0] * ENEMY_MAX
enemy_bullet_a = [0] * ENEMY_MAX
enemy_bullet_type = [0] * ENEMY_MAX
enemy_bullet_speed = [0] * ENEMY_MAX



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
        if bullet_f[i]:
            bullet_x[i] = bullet_x[i] + 36 * math.cos(math.radians((bullet_a[i])))
            bullet_y[i] = bullet_y[i] + 36 * math.sin(math.radians((bullet_a[i])))
            img_rz = pygame.transform.rotozoom(img_player_weapon[0] , -90 - bullet_a[i] , 1.0)
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


def bring_enemy():  # 적 기체 등장
    if timer % 30 == 0:
        set_enemy(random.randint(80, 940), LINE_TOP, 90, 0, 6)


def set_enemy(x, y, a, ty, sp):  # 적 기체 설정
    global enemy_no
    while True:
        if not enemy_f[enemy_no]:
            enemy_f[enemy_no] = True
            enemy_x[enemy_no] = x
            enemy_y[enemy_no] = y
            enemy_a[enemy_no] = a
            enemy_type[enemy_no] = ty
            enemy_speed[enemy_no] = sp
            break
        enemy_no = (enemy_no + 1) % ENEMY_MAX

def set_enemy_bullet(x, y, a, ty, sp):  # 적 기체 설정
    global enemy_bullet_no
    while True:
        if not enemy_f[enemy_bullet_no]:
            enemy_bullet_f[enemy_bullet_no] = True
            enemy_bullet_x[enemy_bullet_no] = x
            enemy_bullet_y[enemy_bullet_no] = y
            enemy_bullet_a[enemy_bullet_no] = a
            enemy_bullet_type[enemy_bullet_no] = ty
            enemy_bullet_speed[enemy_bullet_no] = sp
            break
        enemy_bullet_no = (enemy_bullet_no + 1) % ENEMY_BULLET_MAX




def move_enemy(screen):
    for i in range(ENEMY_MAX):
        if enemy_f[i] == True:
            ang = -90 - enemy_a[i]
            png = enemy_type[i]
            enemy_x[i] = enemy_x[i] + enemy_speed[i] * math.cos(math.radians(enemy_a[i]))
            enemy_y[i] = enemy_y[i] + enemy_speed[i] * math.sin(math.radians(enemy_a[i]))

            if enemy_type[i] == 0 and enemy_y[i] > 360:
                set_enemy_bullet(enemy_x[i], enemy_y[i], 90, 0, 16)
                enemy_a[i] = -45
                enemy_speed[i] = 16
            if enemy_x[i] < LINE_LEFT or LINE_RIGHT < enemy_x[i] or enemy_y[i] < LINE_TOP or LINE_BOTTOM < enemy_y[i]:
                enemy_f[i] = False

            img_rz = pygame.transform.rotozoom(img_enemy[png], ang, 1.0)
            screen.blit(img_rz, [enemy_x[i] - img_rz.get_width() / 2, enemy_y[i] - img_rz.get_height() / 2])


def move_enemy_bullet(screen):  # 적 기체 이동
    for i in range(ENEMY_BULLET_MAX):
        if enemy_bullet_f[i] == True:
            ang = -90 - enemy_bullet_a[i]
            png = enemy_bullet_type[i]
            #enemy_bullet_x[i] = enemy_bullet_x[i] + enemy_bullet_speed[i] * math.cos(math.radians(enemy_bullet_a[i]))
            enemy_bullet_y[i] = enemy_bullet_y[i] + enemy_bullet_speed[i] * math.sin(math.radians(enemy_bullet_a[i]))
            if enemy_bullet_x[i] < LINE_LEFT or LINE_RIGHT < enemy_bullet_x[i] or enemy_bullet_y[i] < LINE_TOP or LINE_BOTTOM < enemy_bullet_y[i]:
                enemy_bullet_f[i] = False
            img_rz = pygame.transform.rotozoom(img_enemy_weapon[png], ang, 1.0)
            screen.blit(img_rz, [enemy_bullet_x[i] - img_rz.get_width() / 2, enemy_bullet_y[i] - img_rz.get_height() / 2])


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
        bring_enemy()
        move_enemy(screen)
        move_enemy_bullet(screen)

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
