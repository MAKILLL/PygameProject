import numpy as np
import pygame
import sys
import math


BLACK = (0, 0, 0)
YELLOW = (208, 223, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

ROW_COUNT = 7
COLUMN_COUNT = 8

SIZE = 100
RADIUS = int(SIZE / 2 - 5)
width = COLUMN_COUNT * SIZE
height = (ROW_COUNT + 1) * SIZE


def create_board():  # функция создания игровой доски (матрицы)
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):  # функция заполнения ячейки
    board[row][col] = piece


def is_valid_location(board, col):   # функция проверки свободного места в столбце
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):  # функция определения первой свободной ячейки в заданном столбце
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def checking_for_a_draw(board):  # проверка ничьей
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 0:
                return False
    return True


def winning_move(board, piece):  # функция проверки победы
    # Проверка по горизонтали
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece\
                    and board[r][c + 3] == piece:
                return True

    # Проверка по вертикали
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece\
                    and board[r + 3][c] == piece:
                return True

    # Проверка по диогонали
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece\
                    and board[r + 3][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece\
                    and board[r - 3][c + 3] == piece:
                return True


def draw_board(board):  # функция отрисовки доски
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, YELLOW, (c * SIZE, r * SIZE + SIZE, SIZE, SIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c * SIZE + SIZE / 2), int(r * SIZE + SIZE + SIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SIZE + SIZE / 2), height - int(r * SIZE + SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, BLUE, (
                    int(c * SIZE + SIZE / 2), height - int(r * SIZE + SIZE / 2)), RADIUS)
            elif board[r][c] == 3:
                pygame.draw.circle(screen, GREEN, (
                    int(c * SIZE + SIZE / 2), height - int(r * SIZE + SIZE / 2)), RADIUS)
    pygame.display.update()


board = create_board()
game_over = False
turn = 0

pygame.init()

FONT = pygame.font.SysFont("Georgia", 75)

screen = pygame.display.set_mode((width, height))
draw_board(board)
pygame.display.update()


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SIZE / 2)), RADIUS)
            elif turn == 1:
                pygame.draw.circle(screen, BLUE, (posx, int(SIZE / 2)), RADIUS)
            elif turn == 2:
                pygame.draw.circle(screen, GREEN, (posx, int(SIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            move_is_made = False
            pygame.draw.rect(screen, BLACK, (0, 0, width, SIZE))

            # Ход первого игрока
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    move_is_made = True

                    if winning_move(board, 1):
                        label = FONT.render("Игрок 1 победил!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

                    if checking_for_a_draw(board):
                        label = FONT.render("Ничья", 1, WHITE)
                        screen.blit(label, (40, 10))
                        game_over = True

            # Ход второго игрока
            elif turn == 1:
                posx = event.pos[0]
                col = int(math.floor(posx / SIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    move_is_made = True

                    if winning_move(board, 2):
                        label = FONT.render("Игрок 2 победил!", 1, BLUE)
                        screen.blit(label, (40, 10))
                        game_over = True

                    if checking_for_a_draw(board):
                        label = FONT.render("Ничья", 1, WHITE)
                        screen.blit(label, (40, 10))
                        game_over = True

            # Ход третьего игрока
            elif turn == 2:
                posx = event.pos[0]
                col = int(math.floor(posx / SIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 3)
                    move_is_made = True

                    if winning_move(board, 3):
                        label = FONT.render("Игрок 3 победил!", 1, GREEN)
                        screen.blit(label, (40, 10))
                        game_over = True

                    if checking_for_a_draw(board):
                        label = FONT.render("Ничья", 1, WHITE)
                        screen.blit(label, (40, 10))
                        game_over = True

            draw_board(board)
            if move_is_made:
                turn += 1
                turn = turn % 3

            if game_over:
                pygame.time.wait(3000)
