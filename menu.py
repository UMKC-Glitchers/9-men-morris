import pygame
import sys
import constants


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Nine Men's Morris - Menu")
        self.clock = pygame.time.Clock()
        self.selected_option = None
        self.font = pygame.font.Font(None, 36)

    def display_menu(self):
        while self.selected_option is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        self.selected_option = 'human_vs_human'
                    elif event.key == pygame.K_c:
                        self.selected_option = 'human_vs_computer'

            self.screen.fill(constants.WHITE)
            text = self.font.render("Nine Men's Morris - Menu", True, constants.BLACK)
            text_rect = text.get_rect(center=(constants.SCREEN_WIDTH / 2, 100))
            self.screen.blit(text, text_rect)

            text_hvh = self.font.render("Press H for - Human vs Human", True, constants.BLACK)
            text_hvc = self.font.render("Press C for - Human vs Computer", True, constants.BLACK)
            self.screen.blit(text_hvh, (constants.SCREEN_WIDTH / 4, 200))
            self.screen.blit(text_hvc, (constants.SCREEN_WIDTH / 4, 250))

            pygame.display.flip()
            self.clock.tick(30)

    def get_selected_option(self):
        return self.selected_option
