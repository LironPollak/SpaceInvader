import pygame


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('icons/basic_enemy.png')
        self.x_change = 0.5
        self.y_change = 10

    def set_enemy(self, screen):
        screen.blit(self.image, (self.x, self.y))
