class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        This function is the main function that solves the Sudoku puzzle.
        It does not return anything, but modifies the board in-place.
        """

        def solve(board):
            """
            This function attempts to solve the Sudoku puzzle recursively.
            It iterates over each cell in the board, and if the cell is empty ('.'), it tries to fill it with a number.
            """
            for row in range(9):  # Iterate over each row
                for column in range(9):  # Iterate over each column
                    if board[row][column] == '.':  # If the cell is empty
                        for num in '123456789':  # Try each number from 1 to 9
                            if isValid(board, row, column, num):  # If the number is valid in the current cell
                                board[row][column] = num  # Insert the number
                                if solve(board):  # Recursively try to solve the rest of the board
                                    return True  # If the board is solved, return True
                                else:
                                    board[row][column] = '.'  # If not, undo the insertion
                        return False  # If no number can be inserted in the current empty cell, return False
            return True  # If the entire board is filled, return True

        def isValid(board, row, col, num):
            """
            This function checks if a number is valid in a certain cell.
            It checks the row, column, and 3x3 box of the cell.
            """
            for i in range(9):  # Iterate over each cell in the row, column, and 3x3 box
                if board[i][col] == num:  # If the number already exists in the column
                    return False
                if board[row][i] == num:  # If the number already exists in the row
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3] == num:  # If the number already exists in the 3x3 box
                    return False
            return True  # If the number does not exist in the row, column, and 3x3 box, it is valid

        solve(board)  # Start solving the Sudoku puzzle



'''


**Time Complexity:**

The time complexity of this algorithm is primarily determined by the number of valid placements for digits in the empty cells. In the worst-case scenario, we would have to explore all possible combinations of numbers in each empty cell. 

Since there are at most 81 cells in a 9x9 Sudoku board, and each cell can contain any digit from 1 to 9, the upper bound of the time complexity can be approximated as $$O(9^{81})$$.

However, this is a very loose upper bound. The actual number of possibilities is significantly less due to the constraints of the Sudoku game (each number can only appear once in each row, column, and 3x3 box). 

**Space Complexity:**

The space complexity of this algorithm is $$O(1)$$, or constant, because the algorithm only uses a fixed amount of space to store the Sudoku board. The board has a fixed size (9x9), and we only use a small amount of additional space for function call stack during recursion (which can be as deep as the number of empty cells in the board).

Please note that these are rough estimates and the actual time and space complexity can vary based on the specific configuration of the Sudoku board (i.e., the initial distribution of numbers and the number of empty cells). The time complexity, in particular, can be significantly less than the upper bound in practice.
'''