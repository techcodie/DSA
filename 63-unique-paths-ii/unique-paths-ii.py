class Solution:
    def rec(self, r, c, obstacleGrid, m, n, dp):
        if r == m and c == n:
            return 1
        if r > m or c > n or obstacleGrid[r][c] == 1:
            return 0
        if dp[r][c] != -1:
            return dp[r][c]
        dp[r][c] = self.rec(r, c + 1, obstacleGrid, m, n, dp) + self.rec(r + 1, c, obstacleGrid, m, n, dp)
        return dp[r][c]

    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        dp = [[-1] * n for _ in range(m)]
        return self.rec(0, 0, obstacleGrid, m - 1, n - 1, dp)