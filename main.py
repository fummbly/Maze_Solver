from graphics import Window
from cell import Cell

def main():
    win = Window(800, 400)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell3 = Cell(win)


    cell1.draw(70, 80, 100, 110)
    cell2.draw(30, 40, 64, 89)
    cell3.draw(120, 330, 500, 300)

    cell2.draw_move(cell3)


    win.wait_for_close()


if __name__ == "__main__":
    main()
