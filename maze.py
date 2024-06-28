import time
from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))

            self._cells.append(col_cells)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        x1 = (self.__cell_size_x * i) + self.__x1
        y1 = (self.__cell_size_y * j) + self.__y1
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)
