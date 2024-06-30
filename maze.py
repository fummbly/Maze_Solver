from functools import total_ordering
import time
from cell import Cell
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__seed = seed
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)


    def _create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))

            self._cells.append(col_cells)
        
        
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        
        self._cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []

            if i - 1 > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if j - 1 > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j -1))
            if i + 1 < self.__num_cols and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j + 1 < self.__num_rows and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            if self.__seed:
                random.seed(self.__seed)

            direction = random.randrange(len(to_visit))

            next_index = to_visit[direction]

            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            elif next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            elif next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            elif next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            self._break_walls_r(next_index[0], next_index[1]) 





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
