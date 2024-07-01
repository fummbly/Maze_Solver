from graphics import Window
from maze import Maze


def main():
    win = Window(800, 400)

    maze = Maze(10, 10, 20, 20, 30, 30, win)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
