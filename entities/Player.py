import pygame
from entities.Missile import Missile


class Player:

    image = pygame.image.load('icons/main_spaceship.png')
    x = 370
    y = 480
    x_change = 0
    y_change = 0
    missile = Missile()

    def set_player(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def fire_missile(self, screen):
        self.missile.fire_missile(screen)
