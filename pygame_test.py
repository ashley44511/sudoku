# how to work pygame based on Tic Tac Toe GUI videos
# in pycharm, go to file > settings > project > interpreter > click + and install "pygame" package
import pygame
import sys
from board import *

# constants
WIDTH = 594
HEIGHT = 594
BG_COLOR = (100, 100, 100)  # rgb values
SQ_SIZE = 66  # size of a square in a 9x9 sudoku board
# pixel coordinates start from top left corner of screen (0,0)
# x goes right and y goes down
BOARD_ROWS = 9
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 5
NUMBER_COLOR = (20, 30, 100)

# pygame template
pygame.init()  # initialize pygame module
pygame.display.set_caption("Tic Tac Toe")  # title of window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # size of screen window
screen.fill(BG_COLOR)  # change background color

# initialize board (from tictactoe)
# board = initialize_board()
# we should make a mark_sqaure function because it is easier to
# use with smaller coords of 0-9 instead of pixels
# mark_square(board, 0, 0, 'x') # marks position with an x
game_over = False

# want 8 horiz lines in Sudoku


def draw_lines():
    # draw horizontal lines
    for i in range(1, BOARD_ROWS):
        # 3rd parameter: starting point, 4th: ending point
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQ_SIZE),
                         (WIDTH, i * SQ_SIZE), LINE_WIDTH)

    # draw vertical lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (i * SQ_SIZE, 0),
                         (i * SQ_SIZE, HEIGHT), LINE_WIDTH)


# call after fill(BG_COLOR)
draw_lines()

chip_font = pygame.font.Font(None, 40)  # None is default font, font size


def draw_chips():
    # 1. define text (surf)

    # determine x and y coords of board

    # for row in range(BOARD_ROWS):
    #     for col in range(BOARD_ROWS):
    #         if board[row][col] == 'x':
    #             # define location, draw x
    #             pass
    #         elif board[row][col] == 'o':
    #             # define loaction, draw o
    #             pass

    # draw 'x' or 'o' as text in window/board
    # define the text
    chip_one_surf = chip_font.render('1', 0, NUMBER_COLOR)
    # define the location; everything you draw is enclosed by rectangle
    # this one is positioned in middle of board
    chip_one_rect = chip_one_surf.get_rect(center=(297, 297))
    # draw (blit) on screen
    screen.blit(chip_one_surf, chip_one_rect)

    # repeat for each number 2-9
    # continues to overlay over already drawn numbers if you put in same spot


draw_chips()


def draw_game_over_screen(winner):
    # draws a game over screen with message
    screen.fill(BG_COLOR)  # makes new screen (no board)
    if winner != 0:
        end_text = f"Player {winner} wins!"
    else:
        end_text = "No one wins!"
    end_surf = font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get.rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(end_surf, end_rect)

    # restart game
    restart_text = "Press r to play again."
    restart_surf = font.render(restart_text, 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 200))
    screen.blit(restart_surf, restart_rect)


while True:
    # want window to be showing up in screen until something happens
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # click X button
            pygame.quit()
            sys.exit()
        # listen for mouse click
        # make sure game isn't over because don't want user to be able to
        # input anything when the game is over
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            print(event.pos)  # position of mouse click
            x, y = event.pos  # unpack x,y coords with tuple
            row = y // SQ_SIZE
            col = x // SQ_SIZE
            print(row, col)  # gives square mouse clicked in

            # given available_square() function in tictactoe files
            # also given mark_square() function
            # if available_square(board, row, col):
            # records it in board list thing
            # mark_square(board, row, col, chip)

            # # check if winner
            # # function provided in tictactoe files
            # if check_if_winner(board, chip):
            # game_over = True
            # winner = player
            # else:
            # if board_is_full(board):
            # game_over = True
            # winner = 0 # tie

            # # tictactoe: alternate between players and chips (we only want to alternate between chips (nums) based on keyboard input)
            # player = 2 if player == 1 else 1
            # chip = 'o' if chip == 'x' else 'o'

            # # draws it on screen
            # draw_chips()
        if event.type == pygame.KEYDOWN:
            # press r key
            if event.key == pygame.K_r:
                screen.fill(BG_COLOR)  # to get rid of end text
                draw_lines()
                board = initialize_board()
                game_over = False
                chip = "x"
                player = 1
                winner = 0

    if game_over:
        pygame.display.update()  # allows last chip to be drawn before game over screen
        # delays for 1s to let player see last chip placed
        pygame.time.delay(1000)
        draw_game_over_screen(winner)

    pygame.display.update()  # allows you to update things on screen

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
# print_hi('PyCharm')
