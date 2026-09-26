import numpy as np

from tetris.experiments import Board


def render_in_numpy(board: Board):
    n = board.n
    m = board.m
    board = np.zeros((n, m))
    # on a numpy array the coordinates start from the upper left.
    # the x axis is the array[:, x] (columns) and as it goes on the right it increases
    # the y axis is the array[y, :] (rows) and it goes down it increases (because number starts from upper left)
    # so in order to get display a (x, y) point, we reverse the order (x, y) -> (y, x)
    # and for y we reverse the orientation ( y -> 5-y)
    for point in board.points:
        point_to_render = np.array(point)
        board[n - point_to_render[1], point_to_render[0]] = 1

    # print(board)
    # board = np.zeros((6, 6))
    # for point in self.X:
    #     point_to_render = np.array([3, 3]) + point
    #     # on a numpy array the coordinates start from the upper left.
    #     # the x axis is the array[:, x] (columns) and as it goes on the right it increases
    #     # the y axis is the array[y, :] (rows) and it goes down it increases (because number starts from upper left)
    #     # so in order to get display a (x, y) point, we reverse the order (x, y) -> (y, x)
    #     # and for y we reverse the orientation ( y -> 5-y)
    #     board[5 - point_to_render[1], point_to_render[0]] = 1
    # print(board)
