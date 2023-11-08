import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BUTTON_COLOR = (0, 128, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)
LIGHT_BROWN = (222, 184, 135)  # Light brown color

# Create the Pygame window for the menu page
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Nine Men's Morris - Menu Page")

# Load the background image
background_image = pygame.image.load("Resources/board1.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a font for the menu options
font = pygame.font.Font(None, 36)

# Create the "Computer vs Human" and "Human vs Human" buttons
button_width = 400
button_height = 80
button_padding = 20  # Padding between buttons
button_x = (SCREEN_WIDTH - button_width) // 2
cvh_button = pygame.Rect(button_x, 250, button_width, button_height)
hvh_button = pygame.Rect(button_x, 250 + button_height + button_padding, button_width, button_height)

# Initialize the selected mode to None
selected_mode = None

notification_text = None  # Variable to store the notification text
notification_rect = None  # Variable to store the notification text rectangle

while True:
    screen.fill(WHITE)

    # Draw the faded or blurred background
    # Adjust the alpha value to control the transparency
    background_image.set_alpha(100)
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if cvh_button.collidepoint(x, y):

                # Display a notification as an alert
                notification_font = pygame.font.Font(None, 24)
                notification_text = notification_font.render("Would be implemented in phase 3", True, LIGHT_BROWN)
                notification_rect = notification_text.get_rect(center=(SCREEN_WIDTH // 2, 500))
            if hvh_button.collidepoint(x, y):

                # Transition to the game GUI with the selected mode
                exec(open('main.py').read())

    # Draw the menu options background (light brown)
    pygame.draw.rect(screen, LIGHT_BROWN, cvh_button)
    pygame.draw.rect(screen, LIGHT_BROWN, hvh_button)

    # Draw the menu options
    cvh_text = font.render("Computer vs Human (Disabled)", True, (128, 128, 128))  # Grayed out text
    hvh_text = font.render("Human vs Human", True, (0, 0, 0))
    cvh_text_rect = cvh_text.get_rect(center=cvh_button.center)
    hvh_text_rect = hvh_text.get_rect(center=hvh_button.center)
    screen.blit(cvh_text, cvh_text_rect)
    screen.blit(hvh_text, hvh_text_rect)

    # Draw the notification as an alert
    if notification_text:
        pygame.draw.rect(screen, (255, 0, 0), notification_rect, border_radius=5)
        screen.blit(notification_text, notification_rect)

    pygame.display.flip()
