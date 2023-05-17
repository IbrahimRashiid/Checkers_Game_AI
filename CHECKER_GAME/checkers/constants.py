import pygame

# board constants
WIDTH, HEIGHT = 800, 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS

# colors
OFFWHITE = (255, 204, 135)
BROWN = (102, 51, 0)
OUTLINECOLOR = (128, 128, 128)
AI_AGENT = (26, 22, 7)  # aka white
COMPUTER = (238, 220, 148)  # aka black
GREEN = (0, 255, 0)
CROWN = pygame.transform.scale(pygame.image.load('assets/king.png'), (54, 35))
