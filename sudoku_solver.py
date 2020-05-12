import numpy as np
import time


class Sudoku:
    @classmethod
    def solve_sudoku_puzzle(cls, sudoku_puzzle):
        for i in range(1, 10):
            if cls.recursive_solver(sudoku_puzzle, i, 0, 0):
                return True
        return False

    @classmethod
    def solve_sudoku_puzzle_timer(cls, sudoku_puzzle):
        start_time = time.time()
        solve_result = cls.solve_sudoku_puzzle(sudoku_puzzle)
        print("Solving time: %s seconds" % (time.time() - start_time))
        return solve_result

    @staticmethod
    def recursive_solver(sudoku_problem, suggested_num, row, column):
        if row >= 9:
            return True
        if column >= 9:
            return Sudoku.recursive_solver(sudoku_problem, suggested_num, row + 1, 0)

        if sudoku_problem[row][column] != 0:
            return Sudoku.recursive_solver(sudoku_problem, suggested_num, row, column + 1)

        if Sudoku.is_number_free(sudoku_problem, suggested_num, row, column):
            for i in range(1, 10):
                sudoku_problem[row][column] = suggested_num
                if not Sudoku.recursive_solver(sudoku_problem, i, row, column + 1):
                    sudoku_problem[row][column] = 0
                else:
                    return True
        else:
            return False

    @staticmethod
    def is_number_free(sudoku_grid, number, row, column):
        for i in range(9):  # check the cross
            if sudoku_grid[row][i] == number or sudoku_grid[i][column] == number:
                return False
        r_block = int(np.floor(row / 3))
        c_block = int(np.floor(column / 3))
        for i in range(3):  # test the block
            for j in range(3):
                if sudoku_grid[r_block * 3 + i][c_block * 3 + j] == number:
                    return False
        return True


sudoku_game_1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudoku_game_2 = [[0, 0, 0, 0, 0, 0, 2, 0, 0],
                 [0, 8, 0, 0, 0, 7, 0, 9, 0],
                 [6, 0, 2, 0, 0, 0, 5, 0, 0],
                 [0, 7, 0, 0, 6, 0, 0, 0, 0],
                 [0, 0, 0, 9, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 4, 0],
                 [0, 0, 5, 0, 0, 0, 6, 0, 3],
                 [0, 9, 0, 4, 0, 0, 0, 7, 0],
                 [0, 0, 6, 0, 0, 0, 0, 0, 0]]

if Sudoku.solve_sudoku_puzzle_timer(sudoku_game_2):
    print(np.matrix(sudoku_game_2))
print("Done")
