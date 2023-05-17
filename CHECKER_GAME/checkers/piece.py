import pygame
from checkers.constants import CROWN, OFFWHITE, OUTLINECOLOR, SQUARE_SIZE


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.isKing = False
        if self.color == OFFWHITE:
            self.direction = 1
        else:
            self.direction = -1

        self.x = 0
        self.y = 0
        self.calculate_position()

    def get_column(self):
        return self.col

    def get_row(self):
        return self.row

    def calculate_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.isKing = True

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position()

    # draw pieces
    def pieces_shape(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, OUTLINECOLOR, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.isKing:
            win.blit(CROWN, (self.x - CROWN.get_width() / 2, self.y - CROWN.get_height() / 2))

    def repair(self):
        return str(self.color)

    def is_king(self):
        return self.isKing
