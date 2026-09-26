import sys
import time

from tetris.game_objects import LShape, Board
from tetris.render import render_in_numpy, draw_grid

from blessed import Terminal


def main():

    n, m = 10, 10

    term = Terminal()

    board = Board(n, m)
    l_shape = LShape(p=[2, 8], n=n, m=m)

    with term.fullscreen(), term.hidden_cursor(), term.cbreak():
        print(term.clear(), end='')
        sys.stdout.flush()

        while board.shape_can_continue(l_shape):
            input_key = term.inkey(timeout=1)

            if input_key:
                if input_key.lower() == 'r':
                    l_shape.rotate()
                elif input_key.name == "KEY_LEFT":
                    l_shape.move_left()
                elif input_key.name == "KEY_RIGHT":
                    l_shape.move_right()

            l_shape.make_next_step()

            grid = render_in_numpy(board, l_shape)
            draw_grid(term, grid)

        time.sleep(5)
    sys.stdout.flush()


if __name__ == '__main__':
    main()


