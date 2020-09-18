import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

coll_blood1 = False
coll_blood2 = False
coll_blood3 = False
coll_blood4 = False
coll_blood5 = False
coll_blood6 = False
coll_blood7 = False

player_img = pygame.image.load('rocket-launch.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6
m = 0

for i in range(no_of_enemies):
    enemy_img.append(pygame.image.load('spaceship.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# blood
bloodX = 100
bloodY = 100
bloodC = 20
blood_state = "ready"
blood_img = pygame.image.load('blood.png')
big_bang = False
enemy_blood = 20
games = "no"

bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
background = pygame.image.load('background.png')

v = "no"
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

big_img = pygame.image.load('alien.png')

over_font = pygame.font.Font('freesansbold.ttf', 64)

exp = pygame.image.load('explosion.png')


def show_exp(x, y):
    screen.blit(exp, (x, y))
    screen.blit(exp, (x + 20, y + 20))
    screen.blit(exp, (x + 40, y + 40))
    screen.blit(exp, (x - 20, y - 10))
    screen.blit(exp, (x - 40, y - 20))
    screen.blit(exp, (x + 60, y + 30))
    screen.blit(exp, (x + 80, y + 40))
    screen.blit(exp, (x - 60, y - 50))
    screen.blit(exp, (x - 80, y - 30))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def big_enemy(x, y):
    screen.blit(big_img, (x, y))


def show_won(x, y):
    score = over_font.render("YOU WON ", True, (0, 255, 0))
    screen.blit(score, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 20, y + 10))


big_eneX = 330
big_eneY = 10
big_eneC = 3


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def enemy_kill(x, y):
    kill = font.render("Enemy_Blood : " + str(enemy_blood), True, (255, 255, 255))
    screen.blit(kill, (x, y))


def game_over():
    game_ov = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_ov, (200, 250))


def iscollision(eX, eY, bX, bY):
    dist = math.sqrt((math.pow(eX - bX, 2)) + (math.pow(eY - bY, 2)))
    if dist < 20:
        return True
    else:
        return False


def ene_iscollision(eX, eY, bX, bY):
    distL = math.sqrt((math.pow((eX - 60) - (bX - 60), 2)) + (math.pow((eY - 60) - (bY - 60), 2)))
    distM = math.sqrt((math.pow(eX - bX, 2)) + (math.pow(eY - bY, 2)))
    distR = math.sqrt((math.pow((eX + 60) - (bX + 60), 2)) + (math.pow((eY + 60) - (bY + 60), 2)))
    if distL < 60 or distR < 60 or distM < 60:
        return True
    else:
        return False


def sound_back(p):
    if p == 0:
        mixer.music.load('backsound.wav')
        mixer.music.play(-1)
    else:
        mixer.music.stop()


def blood_drop(x, y):
    global blood_state
    blood_state = "drop"
    screen.blit(blood_img, (x + 0, y + 20))
    screen.blit(blood_img, (x + 70, y + 20))
    screen.blit(blood_img, (x + 140, y + 20))
    screen.blit(blood_img, (x + 210, y + 20))
    screen.blit(blood_img, (x - 70, y + 20))
    screen.blit(blood_img, (x - 140, y + 20))
    screen.blit(blood_img, (x - 210, y + 20))


sound_back(0)
v = "no"
running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('bullet.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX = playerX + playerX_change
    playerY = playerY + playerY_change

    if playerX >= 736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0

    for i in range(no_of_enemies):
        if enemyY[i] > 440:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
                sound_back(1)
                sun = mixer.Sound('gameover.wav')
                sun.play(-1)
            game_over()
            break

        enemyX[i] = enemyX[i] + enemyX_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] = enemyY[i] + enemyY_change[i]
        elif enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] = enemyY[i] + enemyY_change[i]

        coll = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)

        if coll and big_bang == False:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value = score_value + 1
            if score_value > 24:
                enemyY[i] = -2000
                if score_value == 30:
                    v = "yes"
                    big_bang = True
            else:
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY = bulletY - bulletY_change

    if big_bang == True:
        coll_big = ene_iscollision(big_eneX, big_eneY, bulletX, bulletY)
        if coll_big:
            show_exp(big_eneX, big_eneY)
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value = score_value + 1
            enemy_blood = enemy_blood - 1
            if enemy_blood == 0:
                big_eneX = -2000
                won = mixer.Sound('gamewon.wav')
                won.play()
                show_won(200, 250)
                games = "yes"
                v = "no"
                big_bang = False
    if v == "yes":
        sound_back(1)
        if m == 0:
            mus = mixer.Sound('big_enemy.wav')
            mus.play()
            m = 1
        big_eneX = big_eneX + big_eneC
        if big_eneX <= 0:
            big_eneC = 3
        elif big_eneX >= 600:
            big_eneC = -3
        if blood_state == "ready":
            enemy_coordinates = big_eneX
            blood_state = "drop"
        big_enemy(big_eneX, big_eneY)
    if big_bang == True:
        coll_blood1 = iscollision(playerX, playerY, bloodX, bloodY)
        coll_blood2 = iscollision(playerX, playerY, bloodX + 70, bloodY + 20)
        coll_blood3 = iscollision(playerX, playerY, bloodX + 140, bloodY + 20)
        coll_blood4 = iscollision(playerX, playerY, bloodX + 210, bloodY + 20)
        coll_blood5 = iscollision(playerX, playerY, bloodX - 70, bloodY + 20)
        coll_blood6 = iscollision(playerX, playerY, bloodX - 140, bloodY + 20)
        coll_blood7 = iscollision(playerX, playerY, bloodX - 210, bloodY + 20)

    if coll_blood1 or coll_blood2 or coll_blood3 or coll_blood4 or coll_blood5 or coll_blood6 or coll_blood7:
        sound_back(1)
        sun = mixer.Sound('gameover.wav')
        sun.play(-1)
        big_eneX = -2000
        big_bang = False
        game_over()

    if bloodY >= 600:
        bloodY = 100
        blood_state = "ready"

    if blood_state == "drop":
        bloodX = enemy_coordinates
        bloodY = bloodY + 2
        blood_drop(bloodX, bloodY)

    if big_bang == True:
        enemy_kill(500, 10)

    if games == "yes":
        show_won(230, 250)
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()