from functools import total_ordering
import time
from cell import Cell
import random
from graphics import Line, Point


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self._start = random.randrange(num_cols)
        self._end = random.randrange(num_cols)
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(self._start, 0)
        self._reset_cells_visited()

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
        self._cells[self._start][0].has_top_wall = False
        self._draw_cell(self._start, 0)

        self._cells[self._end][self.__num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._end, self.__num_rows - 1)

    def _reset_cells_visited(self):
        for cols in self._cells:
            for cell in cols:
                cell.visited = False

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:

            to_visit = self._get_valid_directions(i, j)

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

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

    def _get_valid_directions(self, i, j):

        to_visit = []

        if i > 0 and not self._cells[i - 1][j].visited:
            to_visit.append((i - 1, j))
        if j > 0 and not self._cells[i][j - 1].visited:
            to_visit.append((i, j - 1))
        if i + 1 < self.__num_cols and not self._cells[i + 1][j].visited:
            to_visit.append((i + 1, j))
        if j + 1 < self.__num_rows and not self._cells[i][j + 1].visited:
            to_visit.append((i, j + 1))

        return to_visit

    def _draw_cell(self, i, j):
        if self.__win is None:
            return
        x1 = (self.__cell_size_x * i) + self.__x1
        y1 = (self.__cell_size_y * j) + self.__y1
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def solve(self):
        return self.solve_r(self._start, 0)

    def solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if j == self.__num_rows - 1 and not self._cells[i][j].has_bottom_wall:
            return True

        directions = self._get_valid_directions(i, j)

        for direc in directions:

            if (
                    direc[0] == i - 1
                    and not self._cells[i][j].has_left_wall
                    and not self._cells[direc[0]][direc[1]].visited):
                self._cells[i][j].draw_move(
                    self._cells[direc[0]][direc[1]])
                if self.solve_r(direc[0], direc[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(
                        self._cells[direc[0]][direc[1]],
                        True
                    )
            elif (
                    direc[1] == j - 1
                    and not self._cells[i][j].has_top_wall
                    and not self._cells[direc[0]][direc[1]].visited):
                self._cells[i][j].draw_move(
                    self._cells[direc[0]][direc[1]]
                )
                if self.solve_r(direc[0], direc[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(
                        self._cells[direc[0]][direc[1]],
                        True
                    )

            elif (
                direc[0] == i + 1
                and not self._cells[i][j].has_right_wall
                and not self._cells[direc[0]][direc[1]].visited
            ):
                self._cells[i][j].draw_move(
                    self._cells[direc[0]][direc[1]]
                )
                if self.solve_r(direc[0], direc[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(
                        self._cells[direc[0]][direc[1]],
                        True
                    )

            elif (
                direc[1] == j + 1
                and not self._cells[i][j].has_bottom_wall
                and not self._cells[direc[0]][direc[1]].visited
            ):
                self._cells[i][j].draw_move(
                    self._cells[direc[0]][direc[1]]
                )
                if self.solve_r(direc[0], direc[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(
                        self._cells[direc[0]][direc[1]],
                        True
                    )
        return False
