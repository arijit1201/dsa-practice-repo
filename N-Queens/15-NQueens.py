class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initialize an empty chess board
        board = []
        for i in range(n):
            row = '.' * n
            board.append(row)
        result = []

        def isValid(board, row, col):
            # Check if there's a queen in the same row or column
            for i in range(n):
                if (i != col and board[row][i] == "Q") or (i != row and board[i][col] == "Q"):
                    return False

            # Check the diagonals for any other queens
            # Northwest to southeast diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Southwest to northeast diagonal
            r, c = row + 1, col + 1
            while r < n and c < n:
                if board[r][c] == "Q":
                    return False
                r += 1
                c += 1

            # Northeast to southwest diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            # Southeast to northwest diagonal
            r, c = row + 1, col - 1
            while r < n and c >= 0:
                if board[r][c] == "Q":
                    return False
                r += 1
                c -= 1

            return True

        def solve(board, row):
            # If all queens are placed
            if row == n:
                result.append(board.copy())
                return

            # Place queen at every column in the current row, and recur for the next row
            for col in range(n):
                if isValid(board, row, col):
                    # Place queen
                    board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                    # Recur for the next row
                    solve(board, row + 1)
                    # Backtrack and remove the queen from current position
                    board[row] = board[row][:col] + "." + board[row][col + 1 :]

        # Start the algorithm to solve the n-queens problem
        solve(board, 0)
        return result

'''
Explanation for Time and Space Complexity:

TC :
So there are N ways to place queen in first row, n-1 ways in second row and so on.
In worst case, we need to go through all the possible combinations which comes out to be N!
so TC is O(N!)

SC: since it's an NxN chess board it should be N^2 sc
Recursive calls happens N times but it is smaller than N^2 so ultimately SC is O(N^2)
'''