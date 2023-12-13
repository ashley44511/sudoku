# testing for sudoku class methods
import random
from board import Board
from constants import *
import pygame
import sys
from sudoku import *
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku

# test_board
# 7 3 5 6 1 4 8 9 2
# 8 4 2 9 7 3 5 6 1
# 9 6 1 2 8 5 3 7 4
# 2 8 6 3 4 9 1 5 7
# 4 1 3 8 5 7 9 2 6
# 5 7 9 1 2 6 4 3 8
# 1 5 7 4 9 2 6 8 3
# 6 9 4 7 3 8 2 1 5
# 3 2 8 5 6 1 7 4 9
test_board = [[7, 3, 5, 6, 1, 4, 8, 9, 2],
              [8, 4, 2, 9, 7, 3, 5, 6, 1],
              [9, 6, 1, 2, 8, 5, 3, 7, 4],
              [2, 8, 6, 3, 4, 9, 1, 5, 7],
              [4, 1, 3, 8, 5, 7, 9, 2, 6],
              [5, 7, 9, 1, 2, 6, 4, 3, 8],
              [1, 5, 7, 4, 9, 2, 6, 8, 3],
              [6, 9, 4, 7, 3, 8, 2, 1, 5],
              [3, 2, 8, 5, 6, 1, 7, 4, 9]
              ]
empty_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]
               ]
# for i in test_board:
#     print(i)

# valid_in_row test (works)


def valid_in_row(board, row, num):
    # print(num)
    if num in board[row]:
        # print(board[row])
        # checks that num is in a certain row. If it is, return false, because num cannot be valid in that row
        return False
    else:
        # no repeats of num so num can be added to row
        return True


# valid_in_col test (works)
row_length = 9


def valid_in_col(board, col, num):
    valid = True
    for i in range(0, row_length):  # 0 to 9, excluded
        # print(board[i][col])
        if num == board[i][col]:
            valid = False
    return valid

# valid_in_box test (works)


def valid_in_box(board, row_start, col_start, num):
    valid = True
    for i in range(col_start, (col_start + 3)):
        for j in range(row_start, (row_start + 3)):
            # print(board[i][j])
            if board[i][j] == num:
                # checks if duplicate of num in 3x3 box
                valid = False
    return valid

# is_valid test (works)


def is_valid(board, row, col, num):
    valid = False
    if valid_in_row(board, row, num) == True:
        # checks that row is valid. If it is, continue.
        if valid_in_col(board, col, num) == True:
            # checks that col is valid. If it is, continue.

            # finds row_start based on row
            if row < 3:
                row_start = 0
            elif row < 6:
                row_start = 3
            else:
                row_start = 6
            # finds col_start based on col
            if col < 3:
                col_start = 0
            elif col < 6:
                col_start = 3
            else:
                col_start = 6
            if valid_in_box(board, row_start, col_start, num) == True:
                # checks that box is valid. If it is, valid = True.
                valid = True
    return valid

# test fill_box


def fill_box(board, row_start, col_start):
    for i in range(col_start, (col_start + 3)):
        for j in range(row_start, (row_start + 3)):
            found_valid_num = False
            while found_valid_num == False:
                # randint() function found via https://docs.python.org/3/library/random.html
                # a <= int <= b
                # returns a random number from 1-9 inclusive
                rand_num = random.randint(1, 9)
                # checks if rand_num exists in board
                if is_valid(board, j, i, rand_num) == True:
                    board[j][i] = rand_num
                    found_valid_num = True
    return board

# test fill_diagonal


def fill_diagonal(board):
    board = fill_box(board, 0, 0)
    for i in board:
        print(i)
    print()
    board = fill_box(board, 3, 3)
    for i in board:
        print(i)
    print()
    board = fill_box(board, 6, 6)
    for i in board:
        print(i)
    print()
    return board

# remove cells test


def remove_cells(board, removed_cells):
    # easy: 30; medium: 40; hard: 50; get with self.removed_cells
    # selected row and column of user's generated board
    for i in range(removed_cells):
        # finding a row, col coord on board that isn't 0
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        # removing cell value
        board[row][col] = 0


def check_board(board):
    # Check whether the Sudoku board is solved correctly.
    # checking rows
    win = True

    for row in board:
        # print(set(row))
        # print(set(range(1, 10)))
        if set(row) != set(range(1, 10)):
            win = False
            # print(f'win: {win}')
    # checking columns
    for j in range(9):
        col = [board[i][j] for i in range(9)]
        # print("col")
        # print(set(col))
        if set(col) != set(range(1, 10)):
            win = False
    # checks to see if each number appears once in each box
    for i in range(0, 9, 3):
        # print(f'i: {i}')
        for j in range(0, 9, 3):
            subgrid = []
            for x in range(i, i+3):
                for y in range(j, j+3):
                    subgrid.append(board[x][y])
            # print("hi")
            # print(set(subgrid))
            if set(subgrid) != set(range(1, 10)):
                win = False

    return win


if __name__ == "__main__":
    # print(valid_in_row(test_board, 0, 7))

    # print(valid_in_col(test_board, 5, 4))

    # print(valid_in_box(test_board, 0, 6, 1))

    # print(is_valid(test_board, 0, 0, 1))

    # the_board = fill_box(empty_board, 0, 0)
    # for i in the_board:
    # print(i)

    # the_board = fill_diagonal(empty_board)
    # for i in the_board:
    #     print(i)
    # print()

    # FIXME
    # screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # board_class = Board(WIDTH, HEIGHT, screen, "easy")
    # board_class.print_board()

    # removed_cells = 30
    # remove_cells(test_board, removed_cells)
    # for i in test_board:
    #     print(i)

    # generate_sudoku test
    # removed_cells = 30
    # board = generate_sudoku(BOARD_ROWS, removed_cells)
    # print("final board")
    # for i in board:
    # print(i)

    # check_board test
    # print(check_board(empty_board))

    # pygame.init()
    # pygame.display.set_caption("Sudoku")
    # screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # while True:

    #     draw_game_over(screen)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()

    #     pygame.display.update()
