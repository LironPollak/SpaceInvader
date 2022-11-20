import pygame


class GameOver:
    pygame.init()
    x = 200
    y = 300
    font = pygame.font.Font('freesansbold.ttf', 64)

    def show_game_over(self, screen):
        over_text = self.font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (self.x, self.y))
