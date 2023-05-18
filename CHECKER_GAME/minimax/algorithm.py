from copy import deepcopy
import pygame
from checkers.constants import AI_AGENT, COMPUTER

from checkers.piece import Piece
from checkers.board import Board

# # PIECECOLOR1 = (26, 22, 7)
# PIECECOLOR2 = (238, 220, 148)


def minimax(place, depth, max_turn, game):
    if place is None:
        return 0, None
    if depth == 0 or place.who_won(COMPUTER if max_turn else AI_AGENT) is not None:
        return place.evaluation(game.get_turn()), place
    # maximize the score
    if max_turn:
        max_evaluation = float('-inf')
        the_best = None # the best move to the piece
        for move in get_valid_move(place, COMPUTER, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            max_evaluation = max(max_evaluation, evaluation)
            if max_evaluation == evaluation:
                the_best = move
        return max_evaluation, the_best
    # minimize the score
    else:
        min_evaluation = float('inf')
        the_best = None
        for move in get_valid_move(place, AI_AGENT, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            min_evaluation = min(min_evaluation, evaluation)
            if min_evaluation == evaluation:
                the_best = move
        return min_evaluation, the_best


def simulation(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.piece_eat(skip)
    return board


def get_valid_move(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.getAvailableMoves(piece)
        for move, skip in valid_moves.items():
            # show_algorithm(game, board, piece, valid_moves)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulation(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def show_algorithm(game, board, piece, valid_moves):
    valid_moves = board.get_valid_moves(piece)
    board.pieces_shape(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)
