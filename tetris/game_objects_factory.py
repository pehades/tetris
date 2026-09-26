import random

from tetris.game_objects import Shape, LShape, SquareShape


class GameObjectsFactory:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n

    def generate_random_shape(self) -> Shape:

        y = self.n - 2  # generate at the top of the screen
        x = random.randint(2, self.m - 2)
        available_shapes = [LShape(p=[x, y], n=self.n, m=self.m), SquareShape(p=[x, y], n=self.n, m=self.m)]

        shape = random.sample(available_shapes, 1)

        return shape[0]
