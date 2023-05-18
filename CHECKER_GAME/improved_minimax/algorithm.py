from copy import deepcopy
import pygame

from checkers.piece import Piece
from checkers.board import Board

PIECECOLOR1 = (26, 22, 7)
PIECECOLOR2 = (238, 220, 148)


def minimax_improved(place, depth, alpha, beta, max_turn, game):
    if place is None:
        return 0, None
    if depth == 0 or place.who_won(PIECECOLOR2 if max_turn else PIECECOLOR1) is not None:
        return place.evaluation(game.get_turn()), place

    if max_turn:
        max_evaluation = float('-inf')
        the_best = None
        for move in get_valid_move(place, PIECECOLOR2, game):
            evaluation = minimax_improved(move, depth - 1, alpha, beta, False, game)[0]
            max_evaluation = max(max_evaluation, evaluation)
            if max_evaluation == evaluation:
                the_best = move
            alpha = max(alpha, max_evaluation)
            if beta <= alpha:
                break
        return max_evaluation, the_best
    else:
        min_evaluation = float('inf')
        the_best = None
        for move in get_valid_move(place, PIECECOLOR1, game):
            evaluation = minimax_improved(move, depth - 1, alpha, beta, True, game)[0]
            min_evaluation = min(min_evaluation, evaluation)
            if min_evaluation == evaluation:
                the_best = move
            beta = min(beta, min_evaluation)
            if beta <= alpha:
                break
        return min_evaluation, the_best


def simulate_move(piece, move, board, game, skip):
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
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def show_algorithm(game, board, piece, valid_moves):
    valid_moves = board.get_valid_moves(piece)
    board.pieces_shape(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)
