import pygame
import sys
import constants

# Initialize Pygame
pygame.init()


# Valid positions on the board
VALID_POSITIONS = [
    # 0  1  2  3  4  5  6  7
    [0, 0, 0, 0, 0, 0, 0, 0],  # 0
    [0, 3, 0, 3, 0, 3, 0, 0],  # 1
    [0, 0, 3, 3, 3, 0, 0, 0],  # 2
    [0, 3, 3, 0, 3, 3, 0, 0],  # 3
    [0, 0, 3, 3, 3, 0, 0, 0],  # 4
    [0, 3, 0, 3, 0, 3, 0, 0],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0],  # 7
]

LINES = [
    # plus sign pattern
    [3.5, 1.5, 3.5, 2.5],
    [1.5, 3.5, 2.5, 3.5],
    [3.5, 4.5, 3.5, 5.5],
    [4.5, 3.5, 5.5, 3.5],
    # middle square
    [1.5, 1.5, 5.5, 1.5],
    [5.5, 1.5, 5.5, 5.5],
    [5.5, 5.5, 1.5, 5.5],
    [1.5, 5.5, 1.5, 1.5],
    # small square
    [2.5, 2.5, 4.5, 2.5],
    [4.5, 2.5, 4.5, 4.5],
    [4.5, 4.5, 2.5, 4.5],
    [2.5, 4.5, 2.5, 2.5],
]

TOTAL_MENS = 6


class SixMenMorrisBoard:
    def __init__(self, game):
        self.screen = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )
        pygame.display.set_caption("Six Men's Morris")
        self.clock = pygame.time.Clock()
        self.game = game
        self.clicked_point = None

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for x in range(len(LINES)):
            pygame.draw.line(
                self.screen,
                constants.BLACK,
                (
                    LINES[x][0] * constants.SQUARESIZE,
                    constants.SQUARESIZE * LINES[x][1],
                ),
                (
                    LINES[x][2] * constants.SQUARESIZE,
                    LINES[x][3] * constants.SQUARESIZE,
                ),
                5,
            )

        for r in range(constants.ROWS):
            for c in range(constants.COLS):
                radius = constants.CIRCLE_RADIUS
                color = constants.CIRCLE_COLOR
                if int(self.game.CURRENT_POSITION[r][c]) == constants.PLAY1:
                    (color, radius) = (constants.RED, radius)
                elif int(self.game.CURRENT_POSITION[r][c]) == constants.PLAY2:
                    (color, radius) = (constants.BLUE, radius)
                elif int(VALID_POSITIONS[r][c] == constants.VALID):
                    radius = int(constants.CIRCLE_RADIUS / 2)
                else:
                    radius = 0

                pygame.draw.circle(
                    self.screen,
                    color,
                    (
                        int(c * constants.SQUARESIZE + constants.SQUARESIZE / 2),
                        int(r * constants.SQUARESIZE + constants.SQUARESIZE / 2),
                    ),
                    radius,
                )

        # Highlight the selected position
        if self.game.move_made and self.clicked_point:
            r, c = self.clicked_point
            self.draw_highlight(r, c)

        myfont = pygame.font.SysFont("Comic Sans MS", 30)

        label = myfont.render(self.game.message, 1, constants.BLACK)
        self.screen.blit(label, (0.5 * constants.SQUARESIZE, 7 * constants.SQUARESIZE))

        moveLabel = myfont.render(
            "Move made: " + self.game.move_made, 1, constants.BLACK
        )
        self.screen.blit(
            moveLabel, (0.5 * constants.SQUARESIZE, 7.5 * constants.SQUARESIZE)
        )

        player1_pieces = myfont.render(
            "P1:" + str(abs(self.game.play1_counter - TOTAL_MENS)),
            1,
            constants.BLACK,
        )
        self.screen.blit(
            player1_pieces, (7.5 * constants.SQUARESIZE, 0.5 * constants.SQUARESIZE)
        )

        player2_pieces = myfont.render(
            "P2:" + str(abs(self.game.play2_counter - TOTAL_MENS)),
            1,
            constants.BLACK,
        )
        self.screen.blit(
            player2_pieces, (7.5 * constants.SQUARESIZE, 0.8 * constants.SQUARESIZE)
        )

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw_board()

            pygame.display.flip()
            self.clock.tick(60)
