import pygame
import sys
import math
import random
from pygame.locals import *


SCROLLSPEED = 10
BULLET_MAX = 100
ENEMY_MAX = 100
ENEMY_BULLET_MAX = 100
EFFECT_MAX = 100
ITEM_MAX = 100
PLAYER_LIFE = 3
PLAYER_BOMB = 3

SILVER = (192,208,224)
RED = (255,0,0)
CYAN = (0,224,255)


ENEMY_ADS = 1
ENEMY_BOSS = 5

ENEMY_BOSS_BULLET = 0

LINE_TOP = -80
LINE_BOTTOM = 1124
LINE_LEFT = -80
LINE_RIGHT = 1124



img_background = pygame.image.load("image/background3.png")
img_life = pygame.image.load("image/ui/playerLife1_blue.png")
img_bomb = pygame.image.load("image/power-ups/pill_blue.png")


img_item = [
    pygame.image.load("image/power-ups/bolt_gold.png"),
    pygame.image.load("image/power-ups/pill_blue.png")
]

img_ship = [
    pygame.image.load("image/playerShip1_blue.png"),
    pygame.image.load("image/playerShip2_blue.png"),
    pygame.image.load("image/shipFire.png"),
]

img_player_weapon = [
    pygame.image.load("image/lasers/laserRed16.png"), # player laser 1
    pygame.image.load("image/lasers/laserBlue16.png")

]

img_enemy_weapon = [
    pygame.image.load("image/lasers/laserBlue11.png") # enemy laser 1
]

img_enemy = [
    None,
    pygame.image.load("image/enemies/enemyBlack1.png"),
    pygame.image.load("image/enemies/enemy2.png"),
    pygame.image.load("image/enemies/enemy3.png"),
    pygame.image.load("image/enemies/enemy4.png"),
    pygame.image.load("image/enemies/enemy_boss1.png"),
    pygame.image.load("image/enemies/enemy_boss1_f.png")
]

img_explode = [
    None,
    pygame.image.load("image/explosion/boom01.png"),
    pygame.image.load("image/explosion/boom02.png"),
    pygame.image.load("image/explosion/boom03.png"),
    pygame.image.load("image/explosion/boom04.png"),
    pygame.image.load("image/explosion/boom05.png"),
    pygame.image.load("image/explosion/boom06.png"),
    pygame.image.load("image/explosion/boom07.png"),
    pygame.image.load("image/explosion/boom08.png"),
    pygame.image.load("image/explosion/boom09.png"),
    pygame.image.load("image/explosion/boom10.png"),
    pygame.image.load("image/explosion/boom11.png"),
]

img_title = [
    pygame.image.load("image/Title.png")
]

se_barrage = None
se_damage = None
se_explosion = None
se_shot = None




index = 0
timer = 0
score = 0
highscore = 9999
new_record = False
background_ypos = 0

player_x = 0
player_y = 0
player_d = 0
player_invincible = 0
player_life = PLAYER_LIFE
player_bomb = PLAYER_BOMB
player_level = 0

key_space = 0
key_z = 0

bullet_no = 0
bullet_f = [False] * BULLET_MAX
bullet_x = [0] * BULLET_MAX
bullet_y = [0] * BULLET_MAX
bullet_a = [0] * BULLET_MAX
bullet_type = [0] * BULLET_MAX

enemy_no = 0
enemy_f = [False] * ENEMY_MAX
enemy_x = [0] * ENEMY_MAX
enemy_y = [0] * ENEMY_MAX
enemy_a = [0] * ENEMY_MAX
enemy_type = [0] * ENEMY_MAX
enemy_speed = [0] * ENEMY_MAX

item_no = 0
item_f = [False] * ITEM_MAX
item_x = [0] * ITEM_MAX
item_y = [0] * ITEM_MAX
item_a = [0] * ITEM_MAX
item_type = [0] * ITEM_MAX
item_speed = [0] * ITEM_MAX



enemy_bullet_no = 0
enemy_bullet_f = [False] * ENEMY_MAX
enemy_bullet_x = [0] * ENEMY_MAX
enemy_bullet_y = [0] * ENEMY_MAX
enemy_bullet_a = [0] * ENEMY_MAX
enemy_bullet_type = [0] * ENEMY_MAX
enemy_bullet_speed = [0] * ENEMY_MAX
enemy_life = [0] * ENEMY_MAX
enemy_count = [0] * ENEMY_MAX


effect_no = 0
effect_p = [0] * EFFECT_MAX
effect_x = [0] * EFFECT_MAX
effect_y = [0] * EFFECT_MAX


def get_dis(x1,y1,x2,y2):
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

def draw_text(scrn, txt, x, y, siz, col):
    fnt = pygame.font.Font("image/font.ttf", siz)
    sur = fnt.render(txt, True, col)
    x = x - sur.get_width() / 2
    y = y - sur.get_height() / 2
    scrn.blit(sur, [x, y])


def set_bullet(type):
    global bullet_no
    if type == 0:
        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 270
        bullet_type[bullet_no] = 0
        bullet_no = (bullet_no + 1 )%BULLET_MAX

    if type == 1:
        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x - 40
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 270
        bullet_type[bullet_no] = 0
        bullet_no = (bullet_no + 1) % BULLET_MAX

        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 270
        bullet_type[bullet_no] = 0
        bullet_no = (bullet_no + 1) % BULLET_MAX

        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x + 40
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 270
        bullet_type[bullet_no] = 0
        bullet_no = (bullet_no + 1) % BULLET_MAX


    if type == 2:
        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 260
        bullet_type[bullet_no] = 1
        bullet_no = (bullet_no + 1) % BULLET_MAX

        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 270
        bullet_type[bullet_no] = 1
        bullet_no = (bullet_no + 1) % BULLET_MAX

        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 280
        bullet_type[bullet_no] = 1
        bullet_no = (bullet_no + 1) % BULLET_MAX

    if type == 3:
        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x - 40
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 270
        bullet_type[bullet_no] = 0
        bullet_no = (bullet_no + 1) % BULLET_MAX

        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 270
        bullet_type[bullet_no] = 0
        bullet_no = (bullet_no + 1) % BULLET_MAX

        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x + 40
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 270
        bullet_type[bullet_no] = 0
        bullet_no = (bullet_no + 1) % BULLET_MAX

        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 260
        bullet_type[bullet_no] = 1
        bullet_no = (bullet_no + 1) % BULLET_MAX

        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 270
        bullet_type[bullet_no] = 1
        bullet_no = (bullet_no + 1) % BULLET_MAX

        bullet_f[bullet_no] = True
        bullet_x[bullet_no] = player_x
        bullet_y[bullet_no] = player_y - 30
        bullet_a[bullet_no] = 280
        bullet_type[bullet_no] = 1
        bullet_no = (bullet_no + 1) % BULLET_MAX


    if type == 10:
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
            img_rz = pygame.transform.rotozoom(img_player_weapon[bullet_type[i]] , -90 - bullet_a[i] , 1.0)
            screen.blit(img_rz, [bullet_x[i] - img_rz.get_width() / 2 , bullet_y[i] - img_rz.get_height() / 2])
            if bullet_y[i] < 0 or bullet_x[i] < 0 or bullet_x[i] > 960:
                bullet_f[i] = False


def move_ship(screen, key):
    global index, timer,player_x,player_y,player_d,key_space,key_z,player_life,player_invincible,player_bomb,player_level
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
        if player_level == 0:
            set_bullet(0)
        if player_level == 1:
            set_bullet(1)
        if player_level == 2:
            set_bullet(2)
        if player_level == 3:
            set_bullet(3)

        se_shot.play()
    key_z = (key_z + 1) * key[K_z]
    if key_z == 1 and player_bomb > 0:
        set_bullet(10)
        player_bomb -= 1
        se_barrage.play()
    if player_invincible %2 == 0:
        screen.blit(img_ship[2], [player_x - 8, player_y + 40 + (timer % 4) * 2])
        screen.blit(img_ship[player_d] , [player_x - 49, player_y - 37])

    if player_invincible > 0:
        player_invincible = player_invincible - 1
        return
    elif index == 1:
        for i in range(ENEMY_MAX):
            if enemy_f[i] == True:
                w = img_enemy[enemy_type[i]].get_width()
                h = img_enemy[enemy_type[i]].get_height()
                r = int((w + h) / 4 + (74 + 96) / 4)
                if get_dis(enemy_x[i], enemy_y[i], player_x, player_y) < r * r:
                    set_effect(player_x, player_y)
                    player_life -= 1
                    player_level = 0
                    if player_life == 0:
                        index = 2
                        timer = 0
                    if player_invincible == 0:
                        player_invincible = 60
                        se_damage.play()
                    if enemy_type != ENEMY_BOSS:
                        enemy_f[i] = False

        for i in range(ENEMY_BULLET_MAX):
            if enemy_bullet_f[i] == True:
                w = img_enemy_weapon[enemy_bullet_type[i]].get_width()
                h = img_enemy_weapon[enemy_bullet_type[i]].get_height()
                r = int((w + h) / 4 + (74 + 96) / 4)
                if get_dis(enemy_bullet_x[i], enemy_bullet_y[i], player_x, player_y) < r * r:
                    set_effect(player_x, player_y)
                    player_life -= 1
                    if player_life == 0:
                        index = 2
                        timer = 0
                    if player_invincible == 0:
                        player_invincible = 60
                        se_damage.play()
                    enemy_bullet_f[i] = False

        for i in range(ITEM_MAX):
            if item_f[i] == True:
                w = img_item[item_type[i]].get_width()
                h = img_item[item_type[i]].get_height()
                r = int((w + h) / 4 + (74 + 96) / 4)
                if get_dis(item_x[i], item_y[i], player_x, player_y) < r * r:
                    if item_type[i] == 0:
                        if player_level != 3:
                            player_level += 1
                    elif item_type[i] == 1:
                        if player_bomb != 3:
                            player_bomb += 1
                    item_f[i] = False



def bring_enemy():
    sec = timer / 30
    if 0 < sec and sec < 15 and timer % 60 == 0:
        set_enemy(random.randint(20, 940), LINE_TOP, 90, ENEMY_ADS, 8, 1)  # 적 1
        set_enemy(random.randint(20, 940), LINE_TOP, 90, ENEMY_ADS + 1, 12, 1)  # 적 2
        set_enemy(random.randint(100, 860), LINE_TOP, random.randint(60, 120), ENEMY_ADS + 2, 6, 3)  # 적 3
        set_enemy(random.randint(100, 860), LINE_TOP, 90, ENEMY_ADS + 3, 12, 2)  # 적 4
    if timer == 30 * 20:
        set_enemy(480, -210, 90, ENEMY_BOSS, 4, 200)



def set_enemy(x, y, a, ty, sp , lf):
    global enemy_no
    while True:
        if not enemy_f[enemy_no]:
            enemy_f[enemy_no] = True
            enemy_x[enemy_no] = x
            enemy_y[enemy_no] = y
            enemy_a[enemy_no] = a
            enemy_type[enemy_no] = ty
            enemy_speed[enemy_no] = sp
            enemy_life[enemy_no] = lf
            enemy_count[enemy_no] = 0
            break
        enemy_no = (enemy_no + 1) % ENEMY_MAX

def set_enemy_bullet(x, y, a, ty, sp):
    global enemy_bullet_no
    while True:
        if not enemy_bullet_f[enemy_bullet_no]:
            enemy_bullet_f[enemy_bullet_no] = True
            enemy_bullet_x[enemy_bullet_no] = x
            enemy_bullet_y[enemy_bullet_no] = y
            enemy_bullet_a[enemy_bullet_no] = a
            enemy_bullet_type[enemy_bullet_no] = ty
            enemy_bullet_speed[enemy_bullet_no] = sp
            break
        enemy_bullet_no = (enemy_bullet_no + 1) % ENEMY_BULLET_MAX

def set_item(x, y, a, ty, sp):
    global item_no
    while True:
        if not item_f[item_no]:
            item_f[item_no] = True
            item_x[item_no] = x
            item_y[item_no] = y
            item_a[item_no] = a
            item_type[item_no] = ty
            item_speed[item_no] = sp
            break
        item_no = (item_no + 1) % ITEM_MAX




def move_enemy(screen):
    global index , timer , score, highscore , new_record
    for i in range(ENEMY_MAX):
        if enemy_f[i] == True:
            ang = -90 - enemy_a[i]
            png = enemy_type[i]
            if enemy_type[i] != ENEMY_BOSS:
                enemy_x[i] = enemy_x[i] + enemy_speed[i] * math.cos(math.radians(enemy_a[i]))
                enemy_y[i] = enemy_y[i] + enemy_speed[i] * math.sin(math.radians(enemy_a[i]))

                if enemy_type[i] == 1 and enemy_y[i] > 360:
                    set_enemy_bullet(enemy_x[i], enemy_y[i], 90, 0, 12)
                    set_enemy_bullet(enemy_x[i], enemy_y[i], 45, 0, 12)
                    enemy_a[i] = -45
                    enemy_speed[i] = 16

                if enemy_type[i] == 4:
                    enemy_count[i] = enemy_count[i] + 1
                    ang = enemy_count[i] * 10
                    if enemy_y[i] > 240 and enemy_a[i] == 90:
                        enemy_a[i] = random.choice([50, 70, 110, 130])
                        set_enemy_bullet(enemy_x[i], enemy_y[i], random.randint(0,360), 0, 12)


                if enemy_x[i] < LINE_LEFT or LINE_RIGHT < enemy_x[i] or enemy_y[i] < LINE_TOP or LINE_BOTTOM < enemy_y[i]:
                    enemy_f[i] = False

            else: # boss ms
                if enemy_count[i] == 0:
                    enemy_y[i] = enemy_y[i] + 2
                    if enemy_y[i] >= 200:
                        enemy_count[i] = 1
                elif enemy_count[i] == 1:
                    enemy_x[i] = enemy_x[i] - enemy_speed[i]
                    if enemy_x[i] < 200:
                        for j in range(0, 10):
                            set_enemy_bullet(enemy_x[i], enemy_y[i] + 80, j * 20, ENEMY_BOSS_BULLET, 6)
                        enemy_count[i] = 2
                else:
                    enemy_x[i] = enemy_x[i] + enemy_speed[i]
                    if enemy_x[i] > 760:
                        for j in range(0, 10):
                            set_enemy_bullet(enemy_x[i], enemy_y[i] + 80, j * 20, ENEMY_BOSS_BULLET, 6)
                        enemy_count[i] = 1
                if enemy_life[i] < 100 and timer % 30 == 0:
                    set_enemy_bullet(enemy_x[i], enemy_y[i] + 80, random.randint(60, 120), ENEMY_BOSS_BULLET, 6)

            # hit check
            w = img_enemy[enemy_type[i]].get_width()
            h = img_enemy[enemy_type[i]].get_height()
            r = int((w + h)/4) + 12
            er = int((w + h) / 4)
            for n in range(BULLET_MAX):
                if bullet_f[n] == True and get_dis(enemy_x[i],enemy_y[i],bullet_x[n],bullet_y[n]) < r*r:
                    bullet_f[n] = False
                    set_effect(enemy_x[i] + random.randint(-er, er), enemy_y[i] + random.randint(-er, er))
                    if enemy_type[i] == ENEMY_BOSS:  # 보스 기체 깜빡임 처리
                        png = enemy_type[i] + 1
                    se_damage.play()
                    enemy_life[i] -= 1
                    score += 100  # score up
                    if score > highscore:
                        highscore = score
                        new_record = True
                    if enemy_life[i] == 0:
                        enemy_f[i] = False
                        if random.randint(0, 100) <= 20:
                            set_item(enemy_x[i],enemy_y[i],random.randint(50,120),0,10) # random.randint(50,120)
                        if random.randint(0, 100) <= 10:
                            set_item(enemy_x[i],enemy_y[i],random.randint(50,120),1,10) # random.randint(50,120)

                        # drop item randomly

                        if enemy_type[i] == ENEMY_BOSS and index == 1:
                            index = 3
                            timer = 0
                            for j in range(10):
                                set_effect(enemy_x[i] + random.randint(-er, er), enemy_y[i] + random.randint(-er, er))
                            se_explosion.play()

            img_rz = pygame.transform.rotozoom(img_enemy[png], ang, 1.0)
            screen.blit(img_rz, [enemy_x[i] - img_rz.get_width() / 2, enemy_y[i] - img_rz.get_height() / 2])


def move_enemy_bullet(screen):
    for i in range(ENEMY_BULLET_MAX):
        if enemy_bullet_f[i] == True:
            ang = -90 - enemy_bullet_a[i]
            png = enemy_bullet_type[i]
            enemy_bullet_x[i] = enemy_bullet_x[i] + enemy_bullet_speed[i] * math.cos(math.radians(enemy_bullet_a[i]))
            enemy_bullet_y[i] = enemy_bullet_y[i] + enemy_bullet_speed[i] * math.sin(math.radians(enemy_bullet_a[i]))
            if enemy_bullet_x[i] < LINE_LEFT or LINE_RIGHT < enemy_bullet_x[i] or enemy_bullet_y[i] < LINE_TOP or LINE_BOTTOM < enemy_bullet_y[i]:
                enemy_bullet_f[i] = False
            img_rz = pygame.transform.rotozoom(img_enemy_weapon[png], ang, 1.0)
            screen.blit(img_rz, [enemy_bullet_x[i] - img_rz.get_width() / 2, enemy_bullet_y[i] - img_rz.get_height() / 2])

def move_item(screen):
    for i in range(ITEM_MAX):
        if item_f[i] == True:
            ang = 0
            png = item_type[i]
            item_x[i] = item_x[i] + item_speed[i] * math.cos(math.radians(item_a[i]))
            item_y[i] = item_y[i] + item_speed[i] * math.sin(math.radians(item_a[i]))
            if item_x[i] < LINE_LEFT or LINE_RIGHT < item_x[i] or item_y[i] < LINE_TOP or LINE_BOTTOM < item_y[i]:
                item_f[i] = False
            img_rz = pygame.transform.rotozoom(img_item[png], ang, 1.0)
            screen.blit(img_rz, [item_x[i] - img_rz.get_width() / 2, item_y[i] - img_rz.get_height() / 2])



def set_effect(x,y):
    global effect_no
    effect_p[effect_no] = 1
    effect_x[effect_no] = x
    effect_y[effect_no] = y
    effect_no = (effect_no + 1) % EFFECT_MAX


def draw_effect(screen):
    for i in range(EFFECT_MAX):
        if effect_p[i] > 0:
            screen.blit(img_explode[effect_p[i]], [effect_x[i] - 125, effect_y[i] - 125])
            effect_p[i] += 1
            if effect_p[i] == 12:
                effect_p[i] = 0


def draw_ui(screen):
    for i in range(player_life):
        screen.blit(img_life,[60*(i+1),940])

    for i in range(player_bomb):
        screen.blit(img_bomb,[750 + 60*(i+1),940])

    for i in range(player_level):
        screen.blit(img_item[0],[65*(i+1),890 ])






def main():
    global timer , background_ypos , index, score,new_record, player_x , player_y , player_d , player_bomb,player_invincible
    global se_barrage,se_damage,se_explosion,se_shot
    pygame.init()
    pygame.display.set_caption("Space Warrior")
    screen = pygame.display.set_mode((1024,1024))

    clock = pygame.time.Clock()
    se_barrage = pygame.mixer.Sound("sound/barrage.ogg")
    se_damage = pygame.mixer.Sound("sound/damage.ogg")
    se_explosion = pygame.mixer.Sound("sound/explosion.ogg")
    se_shot = pygame.mixer.Sound("sound/shot.ogg")

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
        if index == 0:
            screen.blit(img_title[0],[0,-100])
            draw_text(screen , "Press Space to start",512,512,50,SILVER)
            if key[K_SPACE] == 1:
                index = 1
                timer = 0
                score = 0
                new_record = False
                player_x = 512
                player_y = 960
                player_d = 0
                player_invincible = 0
                for i in range(ENEMY_MAX):
                    enemy_f[i] = False
                for i in range(BULLET_MAX):
                    bullet_f[i] = False
                pygame.mixer.music.load("sound/bgm.ogg")
                pygame.mixer.music.play(-1)


        if index == 1:
            move_ship(screen, key)
            move_bullet(screen)
            move_enemy_bullet(screen)
            bring_enemy()
            move_enemy(screen)
            move_item(screen)

        if index == 2:
            move_bullet(screen)
            move_enemy_bullet(screen)
            move_enemy(screen)
            move_item(screen)
            if timer == 1:
                pygame.mixer.music.stop()
            if timer <= 90:
                if timer % 5 == 0:
                    set_effect(player_x + random.randint(-60, 60), player_y + random.randint(-60, 60))
                if timer % 10 == 0:
                    se_damage.play()
            if timer == 120:
                pygame.mixer.music.load("sound/gameover.ogg")
                pygame.mixer.music.play(0)
            if timer > 120:
                draw_text(screen, "GAME OVER", 480 , 300, 80, RED)
                if new_record == True:
                    draw_text(screen,"NEW RECORD" + str(highscore),480,400,60,CYAN)

            if timer == 400:
                index = 0
                timer = 0

        if index == 3:
            move_ship(screen, key)
            move_bullet(screen)
            move_item(screen)
            if timer == 1:
                pygame.mixer.music.stop()
            if timer < 30 and timer % 2 == 0:
                pygame.draw.rect(screen, (192,0,0),[0,0,1024,1024])
            if timer == 120:
                pygame.mixer.music.load("sound/gameclear.ogg")
                pygame.mixer.music.play(0)
            if timer > 120:
                draw_text(screen , "GAME CLEAR",480 , 300, 80, SILVER)
            if timer == 400:
                index = 0
                timer = 0

        draw_effect(screen)
        draw_text(screen , "SCORE " + str(score) , 200, 30 ,50,SILVER)
        draw_text(screen, "HIGHSCORE " + str(highscore) , 760 , 30 , 50 , CYAN)
        if index != 0:
            draw_ui(screen)



        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
