class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        path = set()
        row = len(board)
        col = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r == row or c == col or            # Short Circuit
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            recursion = (dfs(r + 1, c, i + 1) or
                        dfs(r, c + 1, i + 1) or
                        dfs(r - 1, c, i + 1) or
                        dfs(r, c - 1, i + 1))

            path.remove((r, c))
            return recursion

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True

        return False