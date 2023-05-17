import pygame
from checkers.board import Board
from checkers.constants import GREEN,AI_AGENT, COMPUTER, SQUARE_SIZE
class Game:
    def __init__(self, win,board):
        self.win = win
        self.board = board  # Create a new instance of the Board object
        self.selected = None
        self.turn = AI_AGENT
        self.valid_moves = {}

    def update(self):
        if self.board is not None:
            self.board.draw(self.win)
            self.draw_valid_moves(self.valid_moves)
            pygame.display.update()

    def _initialize(self):
        self.selected = None
        self.board = Board()
        self.turn = COMPUTER
        self.valid_moves = {}

    def winner(self, color):
        if self.board is not None:
            return self.board.is_winner(color)
        else:
            if self.turn == AI_AGENT:
                return "PIECECOLOR2"
            elif self.turn == COMPUTER:
                return "PIECECOLOR1"

    def reset(self):
        self._initialize()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        if self.board is not None:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False

    def _move(self, row, col):
        if self.selected and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.switch_turns()
            return True
        return False

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(
                self.win,
                GREEN,
                (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                10
            )

    def switch_turns(self):
        self.valid_moves = {}
        if self.turn == AI_AGENT:
            self.turn = COMPUTER
        else:
            self.turn = AI_AGENT

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.switch_turns()

    def get_turn(self):
        return self.turn
