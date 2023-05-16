import pygame
from checkers.board import Board
from checkers.constants import WIDTH, HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

pygame.display.set_caption('CHECKERS GAME')

def main():
    pygame.font.init()
    running = True
    clock = pygame.time.Clock()
    board = Board()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.pieces_shape(WIN) 
        pygame.display.update()
    pygame.quit()

main()
