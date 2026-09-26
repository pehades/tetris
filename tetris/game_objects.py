import numpy as np


class Shape:

    def __init__(self, X: np.ndarray, p: np.ndarray, n: int, m: int):
        self.X = X
        self.p = p
        self.n = n
        self.m = m

    @property
    def coordinates(self):
        return self.p + self.X

    def get_next_coordinates(self):
        return self.coordinates + np.array([0, -1])  # move every piece one step down

    def make_next_step(self):
        self.p = self.p + np.array([0, -1])

    def rotate(self):
        new_X = self.X.dot(np.array([[0, -1], [1, 0]]))
        if self.is_inside_board(self.p + new_X):
            self.X = new_X

    def move_right(self):
        new_coordinates = self.coordinates
        if self.is_inside_board(new_coordinates + np.array([[1, 0]])):
            self.p = self.p + np.array([1, 0])

    def move_left(self):
        new_coordinates = self.coordinates
        if self.is_inside_board(new_coordinates + np.array([[-1, 0]])):
            self.p = self.p + np.array([-1, 0])

    def is_inside_board(self, point: np.ndarray) -> bool:
        max_n = int(point[:, 0].max())
        max_m = int(point[:, 1].max())
        return max_n < self.n and max_m < self.m



class LShape(Shape):

    def __init__(self, p: list[float], n: int, m: int):
        super().__init__(X=np.array([[0, -1], [-1, -1], [-1, 0], [-1, 1]]),  p=np.array(p), n=n, m=m)


class Board:

    def __init__(self, n: int, m: int):
        """

        :param n: equals to Y coordinate
        :param m: equals to X coordinate
        """
        self.n = n
        self.m = m
        self.filled_board_coordinates = []

    def shape_can_continue(self, shape: Shape) -> bool:
        next_shape_coordinates = shape.get_next_coordinates()
        for next_coordinate in next_shape_coordinates:
            if next_coordinate in self.filled_board_coordinates or next_coordinate[1] == 0:
                self.add_shape_to_board(shape)
                self.check_and_delete_row()
                return False
        return True

    def add_shape_to_board(self, shape: Shape):
        for next_coordinate in shape.get_next_coordinates():
            self.filled_board_coordinates.append(tuple(next_coordinate))

    def check_and_delete_row(self):
        for row_index in range(self.n):
            coordinates_in_specific_row = [
                filled_coordinate for filled_coordinate in self.filled_board_coordinates if filled_coordinate[1] == row_index
            ]

            if len(coordinates_in_specific_row) == self.m:
                for coordinate in coordinates_in_specific_row:
                    self.filled_board_coordinates.remove(coordinate)



