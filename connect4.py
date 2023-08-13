import sys
import numpy as np
import pygame

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == True

def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # check horizontal locations for win
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][col] == piece and \
                board[row][col + 1] == piece and \
                    board[row][col + 2] == piece and \
                      board[row][col + 3] == piece:
                return True

    # check for vertical locations
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == piece and \
                board[row + 1][col] == piece and \
                    board[row + 2][col] == piece and \
                      board[row + 3][col] == piece:
                return True
            
    # positively sloped diagonals
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == piece and \
                board[row + 1][col + 1] == piece and \
                    board[row + 2][col + 2] == piece and \
                      board[row + 3][col + 3] == piece:
                return True

    # negatively sloped diagonals
    for col in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if board[row][col] == piece and \
                board[row - 1][col + 1] == piece and \
                    board[row - 2][col + 2] == piece and \
                      board[row - 3][col + 3] == piece:
                return True
            
def draw_board(board):
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)



if __name__ == '__main__':
    board = create_board()
    game_over = False
    print_board(board)
    turn  = 0

    pygame.init()

    SQUARE_SIZE = 100
    width = COLUMN_COUNT * SQUARE_SIZE
    height = (ROW_COUNT + 1) * SQUARE_SIZE
    RADIUS = SQUARE_SIZE // 2 - 5   

    screen = pygame.display.set_mode((width, height))
    draw_board(board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == 0:
                    pass
                #     col = int(input('Player 1, make your selection (0-6): '))
                    
                #     if is_valid_location(board, col):
                #         row = get_next_open_row(board, col)
                #         drop_piece(board, row, col, 1)
                    
                #         if winning_move(board, 1):
                #             print('Player 1 wins!')
                #             game_over = True

                # else:
                #     col = int(input('Player 2, make your selection (0-6): '))

                #     if is_valid_location(board, col):
                #         row = get_next_open_row(board, col)
                #         drop_piece(board, row, col, 2)

                #         if winning_move(board, 1):
                #             print('Player 1 wins!')
                #             game_over = True
            
                # print_board(board)
                # turn = (turn + 1) % 2