import sys
import time

from tetris.game_objects_factory import GameObjectsFactory
from tetris.game_objects import LShape, Board
from tetris.render import render_in_numpy, draw_grid

from blessed import Terminal


def main():

    n, m = 10, 10

    term = Terminal()

    board = Board(n, m)
    game_objects_factory = GameObjectsFactory(n, m)

    with term.fullscreen(), term.hidden_cursor(), term.cbreak():
        print(term.clear(), end='')
        sys.stdout.flush()

        shape = game_objects_factory.generate_random_shape()

        while True:
            while board.shape_can_continue(shape):
                input_key = term.inkey(timeout=1)

                if input_key:
                    if input_key.lower() == 'r':
                        shape.rotate()
                    elif input_key.name == "KEY_LEFT":
                        shape.move_left()
                    elif input_key.name == "KEY_RIGHT":
                        shape.move_right()

                shape.make_next_step()

                grid = render_in_numpy(board, shape)
                draw_grid(term, grid)
            shape = game_objects_factory.generate_random_shape()

        time.sleep(5)
    sys.stdout.flush()


if __name__ == '__main__':
    main()


