import pygame
import time

from checkers.board import Board
from checkers.constants import SQUARE_SIZE, WIDTH, HEIGHT, COMPUTER, AI_AGENT
from checkers.checkers import Checkers

from minimax.algorithm import minimax

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

pygame.display.set_caption('CHECKERS GAME')


def get_mouse_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    pygame.font.init()
    running = True
    clock = pygame.time.Clock()
    board = Board()
    game = Checkers(WIN, board)
    depth = 2
  

    while running:
        # time.sleep(0.5)
        clock.tick(FPS)
        if game.turn == AI_AGENT:
            if depth == 1:
                value, new_board1= minimax(game.get_board(), 1, True, game)
            elif depth == 2:
                value, new_board1 = minimax(game.get_board(), 3,  True, game)
            elif depth == 3:
                value, new_board1 = minimax(game.get_board(), 4, True, game)
            game.ai_turn(new_board1)
        else:
            if depth == 1:
                value2, new_board2 = minimax(game.get_board(), 1, False, game)
            elif depth == 2:
                value2, new_board2 = minimax(game.get_board(), 3, False, game)
            elif depth == 3:
                value2, new_board2 = minimax(game.get_board(), 4, False, game)
            game.ai_turn(new_board2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                startPos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(startPos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
