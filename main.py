import pygame
import random
import math
from entities.Enemy import Enemy
from entities.GameOver import GameOver
from entities.Mars import Mars
from entities.Moon import Moon
from entities.Player import Player
from entities.Score import Score
from entities.Earth import Earth

pygame.init()

player = Player()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")
pygame.display.set_icon(player.image)

isGameOver = False
isRunning = True

score = Score()
game_over = GameOver()
earth = Earth()
moon = Moon()
mars = Mars()
enemies = []
num_of_enemies = 50

for i in range(num_of_enemies):
    enemies.append(Enemy(random.randint(50, 750), random.randint(50, 150)))


def is_collision(first_object_x, first_object__y, second_object_x, second_object_y):
    distance = math.sqrt(math.pow(first_object_x - second_object_x, 2) + math.pow(first_object__y - second_object_y, 2))
    return distance < 27


def reset_enemy(enemy_index):
    enemies[enemy_index] = Enemy(random.randint(50, 750), random.randint(50, 150))


while isRunning:
    screen.fill((0, 0, 20))
    screen.blit(moon.image, (moon.x, moon.y))
    screen.blit(earth.image, (earth.x, earth.y))
    screen.blit(mars.image, (mars.x, mars.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player.x_change = 0.5
            if event.key == pygame.K_DOWN:
                player.y_change = 0.5
            if event.key == pygame.K_UP:
                player.y_change = -0.5
            if event.key == pygame.K_SPACE:
                if not player.missile.isFired:
                    player.missile.x = player.x
                    player.missile.y = player.y
                    player.fire_missile(screen)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.y_change = 0

    player.x += player.x_change
    player.y += player.y_change

    if player.x <= 0:
        player.x = 0
    if player.x >= 768:
        player.x = 768
    if player.y <= 0:
        player.y = 0
    if player.y >= 560:
        player.y = 560

    for enemy in range(num_of_enemies):
        if is_collision(player.x, player.y, enemies[enemy].x, enemies[enemy].y):
            for i in range(num_of_enemies):
                enemies[i].y = 2000
            isGameOver = True
            break

        enemies[enemy].x += enemies[enemy].x_change
        if enemies[enemy].x <= 0 or enemies[enemy].x >= 768:
            enemies[enemy].y += enemies[enemy].y_change
            enemies[enemy].x_change *= -1

        if is_collision(enemies[enemy].x, enemies[enemy].y, player.missile.x, player.missile.y):
            player.missile.y = player.y
            player.missile.isFired = False
            score.score += 10
            reset_enemy(enemy)

        enemies[enemy].set_enemy(screen)

    if player.missile.y <= 0:
        player.missile.y = player.y
        player.missile.isFired = False
    if player.missile.isFired:
        player.fire_missile(screen)
        player.missile.y -= player.missile.y_change

    if isGameOver:
        game_over.show_game_over(screen)

    player.set_player(screen)
    score.show_score(screen, score.x, score.y)
    pygame.display.update()
