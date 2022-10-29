import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")
playerImg = pygame.image.load('icons/main_spaceship.png')
pygame.display.set_icon(playerImg)

earthImg = pygame.image.load('icons/earth.png')
marsImg = pygame.image.load('icons/mars.png')
moonImg = pygame.image.load('icons/moon.png')


running = True

player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0

enemyImg = pygame.image.load('icons/basic_enemy.png')
enemy_x = random.randint(50, 750)
enemy_y = random.randint(50, 150)
enemy_x_change = 0.05
enemy_y_change = 10

missileImg = pygame.image.load('icons/missile.png')
missile_x = player_x
missile_y = player_y
missile_x_change = 0
missile_y_change = 0.5
isFired = False


def fire_missile(x, y):
    global isFired
    isFired = True
    screen.blit(missileImg, (x + 16, y + 10))


def set_player(x, y):
    screen.blit(playerImg, (x, y))


def set_enemy(x, y):
    screen.blit(enemyImg, (x, y))


while running:
    screen.fill((0, 0, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            if event.key == pygame.K_DOWN:
                player_y_change = 0.5
            if event.key == pygame.K_UP:
                player_y_change = -0.5
            if event.key == pygame.K_SPACE:
                if not isFired:
                    missile_x = player_x
                    missile_y = player_y
                    fire_missile(missile_x, missile_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0

    player_x += player_x_change
    player_y += player_y_change

    if player_x <= 0:
        player_x = 0
    if player_x >= 768:
        player_x = 768
    if player_y <= 0:
        player_y = 0
    if player_y >= 560:
        player_y = 560

    enemy_x += enemy_x_change

    if enemy_x <= 0 or enemy_x >= 768:
        enemy_y += enemy_y_change
        enemy_x_change *= -1

    if missile_y <= 0:
        missile_y = player_y
        isFired = False
    if isFired:
        fire_missile(missile_x, missile_y)
        missile_y -= missile_y_change

    screen.blit(earthImg, (0, 0))
    screen.blit(moonImg, (50, 500))
    screen.blit(marsImg, (600, 50))
    set_player(player_x, player_y)
    set_enemy(enemy_x, enemy_y)
    pygame.display.update()
