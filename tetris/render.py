import sys

import numpy as np

from tetris.game_objects import Board, Shape


def render_in_numpy(board: Board, shape: Shape):
    n = board.n
    m = board.m
    rendered_board = np.zeros((n, m))
    # on a numpy array the coordinates start from the upper left.
    # the x axis is the array[:, x] (columns) and as it goes on the right it increases
    # the y axis is the array[y, :] (rows) and it goes down it increases (because number starts from upper left)
    # so in order to get display a (x, y) point, we reverse the order (x, y) -> (y, x)
    # and for y we reverse the orientation ( y -> 5-y)
    for point in board.filled_board_coordinates:
        point_to_render = np.array(point)
        rendered_board[n - 1 - point_to_render[1], point_to_render[0]] = 1

    for coordinates in shape.coordinates:
        coordinates_to_render = np.array(coordinates)
        rendered_board[n - 1 - coordinates_to_render[1], coordinates_to_render[0]] = 1

    return rendered_board


def draw_grid(term, numpy_grid):

    for i, row in enumerate(numpy_grid):
        for j, col in enumerate(row):
            print(term.move_xy(j, i) + f"{'_' if col == 0 else 'x'}", end='')

    sys.stdout.flush()
