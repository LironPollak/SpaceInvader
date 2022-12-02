import pygame


class Missile:

    image = pygame.image.load('icons/missile.png')
    x = 370
    y = 480
    x_change = 0
    y_change = 0.5
    isFired = False

    def fire_missile(self, screen):
        self.isFired = True
        screen.blit(self.image, (self.x + 16, self.y + 10))
