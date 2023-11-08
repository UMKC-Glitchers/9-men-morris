import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
MINT_GREEN = (152, 255, 152)

# Create the Pygame window for the start page
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Nine Miles Morris - Start Page")

# Load the background image
background_image = pygame.image.load("Resources/board1.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the start button image
start_button_image = pygame.image.load("Resources/Button.png")
start_button_image = pygame.transform.scale(start_button_image, (200, 80))

# Get the rect of the button image
start_button_rect = start_button_image.get_rect()

# Position the button at the center bottom of the screen
start_button_rect.centerx = SCREEN_WIDTH // 2
start_button_rect.centery = SCREEN_HEIGHT - 50

# Load the font with a larger size
font = pygame.font.Font("Fonts/KidsBoardGame-rqP9.ttf", 40)

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if start_button_rect.collidepoint(x, y):
                # Transition to the menu page
                exec(open('menu.py').read())

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the title at the center top with the font and a larger size
    title_text = font.render("Nine Miles Morris", True,MINT_GREEN)
    title_rect = title_text.get_rect(centerx=SCREEN_WIDTH // 2, top=20)
    screen.blit(title_text, title_rect)

    # Draw the "Start" button
    screen.blit(start_button_image, start_button_rect)

    pygame.display.flip()
