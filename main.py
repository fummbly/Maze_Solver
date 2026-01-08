import random
from graphics import Window
from maze import Maze
import argparse


def main():
    parser = argparse.ArgumentParser(description="Maze solving program")

    parser.add_argument(
        "--rows", type=int, nargs="?", default=20, help="Number of rows in maze"
    )
    parser.add_argument(
        "--cols", type=int, nargs="?", default=20, help="Number of columns in maze"
    )
    parser.add_argument(
        "--seed",
        type=int,
        nargs="?",
        default=random.random(),
        help="Seed for repeatable outputs",
    )

    args = parser.parse_args()

    win = Window(800, 400)

    maze = Maze(10, 10, args.rows, args.cols, 30, 30, win, args.seed)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
