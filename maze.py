import time
from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
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
        
        self._break_entrance_and_exit()
        
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        
        self._cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)


    def _draw_cell(self, i, j):
        if self.__win == None:
            return
        x1 = (self.__cell_size_x * i) + self.__x1
        y1 = (self.__cell_size_y * j) + self.__y1
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.__win == None:
            return
        self.__win.redraw()
        time.sleep(0.05)
