import numpy as _np
import pygame as _pygame
import sys as _sys
import math as _math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	board = _np.zeros((ROW_COUNT, COLUMN_COUNT))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
	for row in range(ROW_COUNT):
		if board[row][col] == 0:
			return row

def print_board(board):
	print(_np.flip(board, 0))

def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diagonals
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diagonals
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			_pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
			_pygame.draw.circle(screen, BLACK, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				_pygame.draw.circle(screen, RED, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				_pygame.draw.circle(screen, YELLOW, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
	_pygame.display.update()


if __name__ == '__main__':
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    _pygame.init()

    SQUARE_SIZE = 100

    width = COLUMN_COUNT * SQUARE_SIZE
    height = (ROW_COUNT+1) * SQUARE_SIZE

    size = (width, height)

    RADIUS = int(SQUARE_SIZE/2 - 5)

    screen = _pygame.display.set_mode(size)
    draw_board(board)
    _pygame.display.update()

    myfont = _pygame.font.SysFont("monospace", 75)

    while not game_over:

        for event in _pygame.event.get():
            if event.type == _pygame.QUIT:
                _sys.exit()

            if event.type == _pygame.MOUSEMOTION:
                _pygame.draw.rect(screen, BLACK, (0,0, width, SQUARE_SIZE))
                posx = event.pos[0]
                if turn == 0:
                    _pygame.draw.circle(screen, RED, (posx, int(SQUARE_SIZE/2)), RADIUS)
                else: 
                    _pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE/2)), RADIUS)
            _pygame.display.update()

            if event.type == _pygame.MOUSEBUTTONDOWN:
                _pygame.draw.rect(screen, BLACK, (0,0, width, SQUARE_SIZE))

                if turn == 0:
                    col = int(_math.floor(event.pos[0]/SQUARE_SIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render("Player 1 wins!!", 1, RED)
                            screen.blit(label, (40,10))
                            game_over = True

                else:				
                    col = int(_math.floor(event.pos[0]/SQUARE_SIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render("Player 2 wins!!", 1, YELLOW)
                            screen.blit(label, (40,10))
                            game_over = True

                print_board(board)
                draw_board(board)

                turn = (turn + 1) % 2

                if game_over:
                    _pygame.time.wait(3000)