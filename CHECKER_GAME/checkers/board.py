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

    # move piece to certain row and column
    def move(self, piece, row, column):
        self.board[piece.row][piece.col], self.board[row][column] = self.board[row][column], self.board[piece.row][piece.col]
        piece.move(row, column)
        # check if the piece became a king
        if row == ROWS - 1 or row == 0:
            if not piece.is_king():
                piece.make_king()
                if piece.color == AI_AGENT:
                    self.PIECECOLOR1_kings += 1
                else:
                    self.PIECECOLOR2_kings += 1

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

    # remove a piece
    def piece_eat(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == AI_AGENT:
                    self.PIECECOLOR1_left -= 1
                else:
                    self.PIECECOLOR2_left -= 1

    def getAvailableMoves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == AI_AGENT or piece.isKing:
            moves.update(self.navigateLeft(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self.navigateRight(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == COMPUTER or piece.isKing:
            moves.update(self.navigateLeft(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self.navigateRight(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def navigateLeft(self, start, stop, step, color, left, skipped=[]): # traverse the board from the left
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            # Empty Tile is Found
            if current == 0:
                # no more tiles available 
                if skipped and not last:
                    break
                elif skipped:
                    # add the skipped part to the previous skipped part in the moves 
                    moves[(r, left)] = last + skipped
                else:
                    # add to the possible moves as soon as an empty tile found
                    moves[(r, left)] = last

                # check if more skippes are availble recurcivly 
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self.navigateLeft(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self.navigateRight(r + step, row, step, color, left + 1, skipped=last))
                break
            #  Tile have piece of the same color 
            elif current.color == color:
                break
            # Tile have piece of different color 
            else:
                # jump over the new tile assuming the tile after it is empty
                last = [current]
                left -= 1
        return moves

    def navigateRight(self, start, stop, step, color, right, skipped=[]): # traverse the board from the right
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            # Empty Tile is Found
            if current == 0:
                # no more tiles available 
                if skipped and not last:
                    break
                elif skipped:
                    # add the skipped part to the previous skipped part in the moves 
                    moves[(r, right)] = last + skipped
                else:
                    # add to the possible moves as soon as an empty tile found
                    moves[(r, right)] = last

                # check if more skippes are availble recurcivly 
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self.navigateLeft(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self.navigateRight(r + step, row, step, color, right + 1, skipped=last))
                break

            #  Tile have piece of the same color 
            elif current.color == color:
                break
            # Tile have piece of different color 
            else:
                # jump over the new tile assuming the tile after it is empty
                last = [current]
                right += 1
        return moves
