import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((6, 7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board

def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

def print_board(board):
    print(np.flip(board, 0))

if __name__ == '__main__':
    board = create_board()
    game_over = False
    print_board(board)
    turn  = 0

    while not game_over:
        if turn == 0:
            col = int(input('Player 1, make your selection (0-6): '))
            
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

        else:
            col = int(input('Player 2, make your selection (0-6): '))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
        print_board(board)
        turn = (turn + 1) % 2