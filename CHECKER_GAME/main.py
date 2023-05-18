import pygame
import time

from checkers.board import Board
from checkers.constants import SQUARE_SIZE, WIDTH, HEIGHT, COMPUTER, AI_AGENT
from checkers.checkers import Checkers
from improved_minimax.algorithm import minimax_improved
from minimax.algorithm import minimax

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

pygame.display.set_caption('CHECKERS GAME')


def get_mouse_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def get_winner(message):
    font = pygame.font.SysFont('comicsans', 60)
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.fill((255, 255, 255))
    WIN.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(3000)


def main():
    pygame.font.init()
    running = True
    clock = pygame.time.Clock()
    board = Board()
    game = Checkers(WIN, board)
    alpha = float('-inf')
    beta = float('inf')
    depth = None
  
    while depth is None:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                depth = 0
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 350 <= pos[0] <= 450 and 150 <= pos[1] <= 200:
                    depth = 1
                elif 350 <= pos[0] <= 450 and 250 <= pos[1] <= 300:
                    depth = 2
                elif 350 <= pos[0] <= 450 and 350 <= pos[1] <= 400:
                    depth = 3

        WIN.fill((255, 255, 255))
        font = pygame.font.SysFont('comicsans', 60)
        title = font.render('Choose Difficulty', True, (0, 0, 0))

        WIN.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        font2 = pygame.font.SysFont('comicsans', 40)
        option1 = font2.render('Easy', True, (0, 0, 0))
        WIN.blit(option1, (WIDTH // 2 - option1.get_width() // 2, 150))

        option2 = font2.render('Medium', True, (0, 0, 0))
        WIN.blit(option2, (WIDTH // 2 - option2.get_width() // 2, 250))

        option3 = font2.render('Hard', True, (0, 0, 0))
        WIN.blit(option3, (WIDTH // 2 - option3.get_width() // 2, 350))

        pygame.display.update()

    while running:
        # time.sleep(0.5)
        clock.tick(FPS)
        if game.turn == AI_AGENT:
            if depth == 1:
                value, new_board2 = minimax_improved(game.get_board(), 1, alpha, beta, True, game)
            elif depth == 2:
                value, new_board2 = minimax_improved(game.get_board(), 3, alpha, beta, True, game)
            elif depth == 3:
                value, new_board2 = minimax_improved(game.get_board(), 4, alpha, beta, True, game)
            game.ai_turn(new_board2)
        else:
            if depth == 1:
                value2, new_board2 = minimax(game.get_board(), 1, False, game)
            elif depth == 2:
                value2, new_board2 = minimax(game.get_board(), 3, False, game)
            elif depth == 3:
                value2, new_board2 = minimax(game.get_board(), 4, False, game)
            game.ai_turn(new_board2)
        message = ''
        if game.who_won(AI_AGENT) == "PIECECOLOR1":
            message = "Black won"
            get_winner(message)
            running = False

        elif game.who_won(COMPUTER) == "PIECECOLOR2":
            message = "White won"
            get_winner(message)
            running = False
        elif game.who_won(COMPUTER) == "no winner" or game.who_won(AI_AGENT) == "no winner":
            message = "no winner"
            get_winner(message)
            running = False

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
