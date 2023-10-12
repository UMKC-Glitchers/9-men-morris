import pygame
import sys
import math
import constants

# Initialize Pygame
pygame.init()


def get_coords(mouse_pos):
    col = int(mouse_pos[0] / constants.SQUARESIZE)
    row = int((mouse_pos[1]) / constants.SQUARESIZE)
    return row, col


class NineMensMorrisGUI:
    def __init__(self, game):
        # Initialize Pygame window
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Nine Men's Morris")
        self.clock = pygame.time.Clock()
        self.game = game
        self.clicked_point = None

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for x in range(len(constants.LINES)):
            pygame.draw.line(self.screen, constants.BLACK,
                             (constants.LINES[x][0] * constants.SQUARESIZE,
                              constants.SQUARESIZE * constants.LINES[x][1]),
                             (constants.LINES[x][2] * constants.SQUARESIZE,
                              constants.LINES[x][3] * constants.SQUARESIZE), 5)

        for r in range(constants.ROWS):
            for c in range(constants.COLS):
                radius = constants.CIRCLE_RADIUS
                color = constants.CIRCLE_COLOR
                if int(self.game.CURRENT_POSITION[r][c]) == constants.PLAY1:
                    (color, radius) = (constants.RED, radius)
                elif int(self.game.CURRENT_POSITION[r][c]) == constants.PLAY2:
                    (color, radius) = (constants.BLUE, radius)
                elif int(constants.VALID_POSITIONS[r][c] == constants.VALID):
                    radius = int(constants.CIRCLE_RADIUS / 2)
                else:
                    radius = 0

                pygame.draw.circle(self.screen, color,
                                   (int(c * constants.SQUARESIZE + constants.SQUARESIZE / 2),
                                    int(r * constants.SQUARESIZE + constants.SQUARESIZE / 2)), radius)

        myfont = pygame.font.SysFont("Comic Sans MS", 30)

        label = myfont.render(self.game.message, 1, constants.BLACK)
        self.screen.blit(label, (.5 * constants.SQUARESIZE, 7 * constants.SQUARESIZE))

        moveLabel = myfont.render("Move made: "+self.game.move_made, 1, constants.BLACK)
        self.screen.blit(moveLabel, (.5 * constants.SQUARESIZE, 7.5 * constants.SQUARESIZE))

    def handle_events(self):
        (r, c) = get_coords(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # elif event.type == pygame.MOUSEMOTION:
            #     print("hovered", r+1, c+1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.game.make_move(r, c, None, None)

    def main_loop(self):
        while True:
            self.draw_board()

            self.handle_events()

            pygame.display.flip()
            self.clock.tick(60)
