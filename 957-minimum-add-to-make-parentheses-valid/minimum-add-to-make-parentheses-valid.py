class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opencnt = 0
        res = 0

        for c in s:
            if c == '(':
                opencnt += 1
            else:
                opencnt -= 1
                if opencnt < 0:
                    res += 1
                    opencnt = 0

        return res + opencnt
        
