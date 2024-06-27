from graphics import Window, Line, Point

def main():
    win = Window(800, 400)
    p1 = Point(0, 0)
    p2 = Point(100, 200)
    p3 = Point(10, 15)
    p4 = Point(12, 25)

    l1 = Line(p1, p2)
    l2 = Line(p3, p4)
    l3 = Line(p4, p2)

    win.draw_line(l1, "black")
    win.draw_line(l2, "red")
    win.draw_line(l3, "green")

    win.wait_for_close()


if __name__ == "__main__":
    main()
