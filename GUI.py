import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions and board
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (0, 0, 0)
CIRCLE_RADIUS = 10

# Board layout
BOARD_LAYOUT = [
    [(100, 100), (400, 100), (700, 100)],
    [(200, 200), (400, 200), (600, 200)],
    [(400, 300)],
    [(100, 400), (200, 400), (300, 400), (500, 400), (600, 400), (700, 400)],
    [(400, 500)],
    [(200, 600), (400, 600), (600, 600)],
    [(100, 700), (400, 700), (700, 700)],
]

# Board layout
BOARD_LAYOUT_HOVER = [
    [0, 0, 0],
    [0, 0, 0],
    [0],
    [0, 0, 0, 0, 0, 0],
    [0],
    [0, 0, 0],
    [0, 0, 0],
]

class NineMensMorrisGUI:
    def __init__(self, game):
        # Initialize Pygame window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Nine Men's Morris")
        self.clock = pygame.time.Clock()
        self.game = game

    def draw_board(self):
        # Draw the board
        self.screen.fill((255, 255, 255))

        # Outer lines
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[0][0], BOARD_LAYOUT[0][2], 5)
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[6][0], BOARD_LAYOUT[6][2], 5)

        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[0][0], BOARD_LAYOUT[6][0], 5)
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[0][2], BOARD_LAYOUT[6][2], 5)

        # Middle lines
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[1][0], BOARD_LAYOUT[1][2], 5)
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[5][0], BOARD_LAYOUT[5][2], 5)

        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[1][0], BOARD_LAYOUT[5][0], 5)
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[1][2], BOARD_LAYOUT[5][2], 5)

        # Inside lines
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[2][0],(500,300), 5)
        pygame.draw.line(self.screen, LINE_COLOR,(300,300), BOARD_LAYOUT[2][0],5)

        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[4][0],(500,500), 5)
        pygame.draw.line(self.screen, LINE_COLOR,(300,500), BOARD_LAYOUT[4][0],5)

        pygame.draw.line(self.screen, LINE_COLOR,(300,300), BOARD_LAYOUT[3][2],5)
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[3][2],(300,500), 5)

        pygame.draw.line(self.screen, LINE_COLOR,(500,300), BOARD_LAYOUT[3][3],5)
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[3][3],(500,500), 5)

        # horizontal lines
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[3][0],BOARD_LAYOUT[3][2], 5)
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[3][3],BOARD_LAYOUT[3][5], 5)

        # Vertical lines
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[0][1],BOARD_LAYOUT[2][0], 5)
        pygame.draw.line(self.screen, LINE_COLOR, BOARD_LAYOUT[4][0],BOARD_LAYOUT[6][1], 5)

        # Draw circles for the positions
        for row in BOARD_LAYOUT:
            for pos in row:
                pygame.draw.circle(self.screen, CIRCLE_COLOR, pos, CIRCLE_RADIUS)

    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                for square in BOARD_LAYOUT:
                    for pos in square:
                        if math.sqrt((pos[0] - mouse_pos[0]) ** 2 + (pos[1] - mouse_pos[1]) ** 2) <= CIRCLE_RADIUS:
                            print("Point hovered:", pos)
                            pygame.draw.circle(self.screen, (200, 200, 200), pos, CIRCLE_RADIUS + 10)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Check for mouse click on points
                    for square in BOARD_LAYOUT:
                        for pos in square:
                            if math.sqrt((pos[0] - mouse_pos[0]) ** 2 + (pos[1] - mouse_pos[1]) ** 2) <= CIRCLE_RADIUS:
                                print("Point clicked:", pos)

    def main_loop(self):
        while True:
            # Draw the board
            self.draw_board()

            self.handle_events()

            pygame.display.flip()
            self.clock.tick(60)
