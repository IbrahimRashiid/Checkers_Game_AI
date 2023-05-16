import pygame
from checkers.constants import BROWN, OFFWHITE, AI_AGENT, COMPUTER, ROWS, SQUARE_SIZE, COLS
from checkers.piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.PIECECOLOR1_left = self.PIECECOLOR2_left = 12
        self.PIECECOLOR1_kings = self.PIECECOLOR2_kings = 0
        self.draw_board()

    # draw squares in the board
    def draw_squares(self, win):
        win.fill(BROWN)
        for row in range(ROWS):
            for column in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, OFFWHITE, (row * SQUARE_SIZE, column * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    # get specific piece with its row and column
    def get_piece(self, row, col):
        return self.board[row][col]

    # creat the board
    def draw_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, COMPUTER))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, AI_AGENT))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    # draw the board
    def pieces_shape(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.pieces_shape(win)
