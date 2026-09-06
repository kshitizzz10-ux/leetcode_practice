class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j):
            # We have matched all of t
            if j == len(t):
                return 1

            # We ran out of s before matching t
            if i == len(s):
                return 0

            # Already calculated this state
            if (i, j) in memo:
                return memo[(i, j)]

            # If characters match, we have two choices
            if s[i] == t[j]:
                use = dfs(i + 1, j + 1)
                skip = dfs(i + 1, j)

                memo[(i, j)] = use + skip

            # If they don't match, we can only skip s[i]
            else:
                memo[(i, j)] = dfs(i + 1, j)

            return memo[(i, j)]

        return dfs(0, 0)