class Solution:
    def solve(self, ans: list[str], s: str, open: int, close: int, n: int) -> None:
        if close == n and open == n:
            ans.append(s)
            return
        if open < n:
            self.solve(ans, s + "(", open + 1, close, n)
        if close < open:
            self.solve(ans, s + ")", open, close + 1, n)
    
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []         
        self.solve(ans, "", 0, 0, n) 
        return ans