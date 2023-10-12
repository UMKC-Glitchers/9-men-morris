# current positions on the board
CURRENT_POSITION = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# Valid positions on the board
VALID_POSITIONS = [
    [3, 0, 0, 3, 0, 0, 3, 0],
    [0, 3, 0, 3, 0, 3, 0, 0],
    [0, 0, 3, 3, 3, 0, 0, 0],
    [3, 3, 3, 0, 3, 3, 3, 0],
    [0, 0, 3, 3, 3, 0, 0, 0],
    [0, 3, 0, 3, 0, 3, 0, 0],
    [3, 0, 0, 3, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

LINES = [
    # plus sign pattern
    [3.5,  .5, 3.5, 2.5],
    [0.5, 3.5, 2.5, 3.5],
    [3.5, 4.5, 3.5, 6.5],
    [4.5, 3.5, 6.5, 3.5],
    # outer square
    [  .5,  .5, 6.5,  .5],
    [ 6.5,  .5, 6.5, 6.5],
    [ 6.5, 6.5,  .5, 6.5],
    [ 0.5, 6.5,  .5,  .5],
    # middle square
    [ 1.5, 1.5, 5.5, 1.5],
    [ 5.5,  1.5, 5.5, 5.5],
    [ 5.5, 5.5,  1.5, 5.5],
    [ 1.5, 5.5, 1.5, 1.5],
    # small square
    [ 2.5, 2.5, 4.5, 2.5],
    [ 4.5,  2.5, 4.5, 4.5],
    [ 4.5, 4.5,  2.5, 4.5],
    [ 2.5, 4.5, 2.5, 2.5],
]

# Board status
BLANK = 0
PLAY1 = 1
PLAY2 = 2
VALID = 3

# board size and pieces
ROWS = 7
COLS = 7

# Constants for the screen dimensions and board
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (0, 0, 0)
CIRCLE_RADIUS = 15

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 155)
GRAY = (200, 200, 200)

SQUARESIZE = 110
