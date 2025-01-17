from graphics import Line, Point


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.visited = False
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        left_wall = Line(Point(self.__x1, self.__y1),
                         Point(self.__x1, self.__y2))
        top_wall = Line(Point(self.__x1, self.__y1),
                        Point(self.__x2, self.__y1))
        right_wall = Line(Point(self.__x2, self.__y1),
                          Point(self.__x2, self.__y2))
        bottom_wall = Line(Point(self.__x1, self.__y2),
                           Point(self.__x2, self.__y2))

        if self.has_left_wall:
            self.__win.draw_line(left_wall, "black")
        else:
            self.__win.draw_line(left_wall, "white")

        if self.has_top_wall:
            self.__win.draw_line(top_wall, "black")
        else:
            self.__win.draw_line(top_wall, "white")

        if self.has_right_wall:
            self.__win.draw_line(right_wall, "black")
        else:
            self.__win.draw_line(right_wall, "white")

        if self.has_bottom_wall:
            self.__win.draw_line(bottom_wall, "black")
        else:
            self.__win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, redo=False):
        if self.__win is None:
            return
        if redo:
            color = "grey"
        else:
            color = "red"

        start = Point((self.__x1 + self.__x2) // 2,
                      (self.__y1 + self.__y2) // 2)
        end = Point((to_cell.__x1 + to_cell.__x2) // 2,
                    (to_cell.__y1 + to_cell.__y2) // 2)

        line = Line(start, end)
        self.__win.draw_line(line, color)
