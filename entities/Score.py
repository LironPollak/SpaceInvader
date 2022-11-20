import pygame


class Score:
    pygame.init()
    x = 370
    y = 10
    score = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    def show_score(self, screen, x, y):
        score_board = self.font.render("Score : " + str(self.score), True, (255, 255, 255))
        screen.blit(score_board, (x, y))
