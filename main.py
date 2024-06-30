from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 400)

    maze = Maze(0, 0, 20, 20, 30, 30, win, 0)





    win.wait_for_close()


if __name__ == "__main__":
    main()
