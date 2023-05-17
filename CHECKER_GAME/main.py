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
    checkers_board = Board()
    checkers_board.move(checkers_board.get_piece(1,2),4,4)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        checkers_board.pieces_shape(WIN) 
        pygame.display.update()
    pygame.quit()

main()

