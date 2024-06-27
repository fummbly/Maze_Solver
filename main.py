from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 400)
    cell1 = Cell(30, 10, 60, 40, win)
    cell2 = Cell(100, 200, 500, 800, win)
    cell3 = Cell(70, 80, 100, 110, win)

    cell1.has_right_wall = False
    cell2.has_top_wall = False
    cell3.has_left_wall = False
    cell3.has_bottom_wall = False

    cell1.draw()
    cell2.draw()
    cell3.draw()


    win.wait_for_close()


if __name__ == "__main__":
    main()
