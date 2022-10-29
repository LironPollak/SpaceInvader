import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")
playerImg = pygame.image.load('icons/main_spaceship.png')
pygame.display.set_icon(playerImg)

earthImg = pygame.image.load('icons/earth.png')
marsImg = pygame.image.load('icons/mars.png')
moonImg = pygame.image.load('icons/moon.png')

isGameOver = False
isRunning = True

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
score_x = 370
score_y = 10

game_over_font = pygame.font.Font('freesansbold.ttf', 64)
game_over_x = 370
game_over_y = 300


def show_score(x, y):
    score_board = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_board, (x, y))


def game_over():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    show_score(300, 400)
    screen.blit(over_text, (200, 300))


player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0

enemyImg = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 50

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('icons/basic_enemy.png'))
    enemy_x.append(random.randint(50, 750))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(0.5)
    enemy_y_change.append(10)

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


def set_enemy(x, y, enemy_index):
    screen.blit(enemyImg[enemy_index], (x, y))


def is_collision(first_object_x, first_object__y, second_object_x, second_object_y):
    distance = math.sqrt(math.pow(first_object_x - second_object_x, 2) + math.pow(first_object__y - second_object_y, 2))
    return distance < 27


def reset_enemy(enemy_index):
    global enemy_x, enemy_y
    enemy_x[enemy_index] = random.randint(50, 750)
    enemy_y[enemy_index] = random.randint(50, 150)


while isRunning:
    screen.fill((0, 0, 20))
    screen.blit(moonImg, (0, 0))
    screen.blit(earthImg, (50, 500))
    screen.blit(marsImg, (600, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

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

    for enemy in range(num_of_enemies):
        if is_collision(player_x, player_y, enemy_x[enemy], enemy_y[enemy]):
            for i in range(num_of_enemies):
                enemy_y[i] = 2000
            isGameOver = True
            break

        enemy_x[enemy] += enemy_x_change[enemy]
        if enemy_x[enemy] <= 0 or enemy_x[enemy] >= 768:
            enemy_y[enemy] += enemy_y_change[enemy]
            enemy_x_change[enemy] *= -1

        if is_collision(enemy_x[enemy], enemy_y[enemy], missile_x, missile_y):
            missile_y = player_y
            isFired = False
            score += 10
            reset_enemy(enemy)

        set_enemy(enemy_x[enemy], enemy_y[enemy], enemy)

    if missile_y <= 0:
        missile_y = player_y
        isFired = False
    if isFired:
        fire_missile(missile_x, missile_y)
        missile_y -= missile_y_change

    if isGameOver:
        game_over()

    set_player(player_x, player_y)
    show_score(score_x, score_y)
    pygame.display.update()
