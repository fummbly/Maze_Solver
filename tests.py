import unittest

from maze import Maze


class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols
        )

        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )


    def test_maze_larger_size(self):
        num_cols = 40
        num_rows = 60
        m1 = Maze(0,0,num_rows, num_cols, 10,10)

        self.assertEqual(
            len(m1._cells),
            num_cols
        )

        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )


if __name__ == "__main__":
    unittest.main()