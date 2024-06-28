from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 400)

    maze = Maze(10, 10, 10, 10, 40, 40, win)





    win.wait_for_close()


if __name__ == "__main__":
    main()
