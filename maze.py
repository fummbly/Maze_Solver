from functools import total_ordering
import time
from cell import Cell
import random
from graphics import Line, Point


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
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

    # Function for creating cells with 4 walls the size of the maze
    def _create_cells(self):
        # Range over columns
        for i in range(self.__num_cols):
            # Initiate an array for the columns
            col_cells = []
            # Range over the rows
            for j in range(self.__num_rows):
                # Append a cell
                col_cells.append(Cell(self.__win))

            self._cells.append(col_cells)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        # Breaking the top wall of the start cell
        self._cells[self._start][0].has_top_wall = False
        self._draw_cell(self._start, 0)

        # Break the bottom wall of the end cell
        self._cells[self._end][self.__num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._end, self.__num_rows - 1)

    # Helper function to reset the visited value of all cells
    def _reset_cells_visited(self):
        for cols in self._cells:
            for cell in cols:
                cell.visited = False

    # Function to recursivly run through each cell and break random walls
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = self._get_valid_directions(i, j)

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            # Get a random direction to go
            direction = random.randrange(len(to_visit))

            # the next index is the random direction in the to visit list
            next_index = to_visit[direction]

            # if x index is less than the current one the direction is left
            if next_index[0] == i - 1:
                # delete the left wall of the current cell
                self._cells[i][j].has_left_wall = False
                # delete the next cells right wall
                self._cells[i - 1][j].has_right_wall = False
            # if the x index is larger than the current one the direction is right
            elif next_index[0] == i + 1:
                # delete the right wall of the current cell
                self._cells[i][j].has_right_wall = False
                # delete the next cells left wall
                self._cells[i + 1][j].has_left_wall = False
            # if the y index is less than the current one the direction is up
            elif next_index[1] == j - 1:
                # delete the top wall of the current cell
                self._cells[i][j].has_top_wall = False
                # delete the bottom wall of the next cell
                self._cells[i][j - 1].has_bottom_wall = False
            # if the y index is greater than the current on the direction is down
            elif next_index[1] == j + 1:
                # delete the bottom wall of the current cell
                self._cells[i][j].has_bottom_wall = False
                # delete the top wall of the next cell
                self._cells[i][j + 1].has_top_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    # function to get all possible directions from a current cell
    def _get_valid_directions(self, i, j):
        to_visit = []

        # if the i index is not on the edge of the left side of the maze and the cell to the left hasn't been visited
        if i > 0 and not self._cells[i - 1][j].visited:
            # add the cell to the left to the array
            to_visit.append((i - 1, j))
        # if the j index is not on the edge of the top edge of the maze and the cell above hasn't been visited
        if j > 0 and not self._cells[i][j - 1].visited:
            # add the above cell to the array
            to_visit.append((i, j - 1))
        # if the i index is not on the edge of the right side of the maze and the cell to the left hasn't been visited
        if i + 1 < self.__num_cols and not self._cells[i + 1][j].visited:
            # add the cell to the right to the array
            to_visit.append((i + 1, j))
        # if the j index is not on the edge of the bottom edge of the maze and the cell bellow hasn't been visited
        if j + 1 < self.__num_rows and not self._cells[i][j + 1].visited:
            to_visit.append((i, j + 1))
            # add the cell bellow to the array

        return to_visit

    # drawing cells function
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
        time.sleep(0.03)

    # solve function
    def solve(self):
        return self.solve_r(self._start, 0)

    # Recursive solve function
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
                and not self._cells[direc[0]][direc[1]].visited
            ):
                self._cells[i][j].draw_move(self._cells[direc[0]][direc[1]])
                if self.solve_r(direc[0], direc[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[direc[0]][direc[1]], True)
            elif (
                direc[1] == j - 1
                and not self._cells[i][j].has_top_wall
                and not self._cells[direc[0]][direc[1]].visited
            ):
                self._cells[i][j].draw_move(self._cells[direc[0]][direc[1]])
                if self.solve_r(direc[0], direc[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[direc[0]][direc[1]], True)

            elif (
                direc[0] == i + 1
                and not self._cells[i][j].has_right_wall
                and not self._cells[direc[0]][direc[1]].visited
            ):
                self._cells[i][j].draw_move(self._cells[direc[0]][direc[1]])
                if self.solve_r(direc[0], direc[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[direc[0]][direc[1]], True)

            elif (
                direc[1] == j + 1
                and not self._cells[i][j].has_bottom_wall
                and not self._cells[direc[0]][direc[1]].visited
            ):
                self._cells[i][j].draw_move(self._cells[direc[0]][direc[1]])
                if self.solve_r(direc[0], direc[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[direc[0]][direc[1]], True)
        return False
