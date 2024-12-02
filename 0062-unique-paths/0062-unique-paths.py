class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def solve(row, col, memo = {}):
            if row > m or col > n:
                return 0

            if row == m - 1 and col == n - 1:
                return 1

            if (row, col) in memo:
                return memo[(row, col)]

            down = solve(row + 1, col, memo)
            right = solve(row, col + 1, memo)

            memo[(row, col)] = down + right

            return down + right

        return solve(0, 0)