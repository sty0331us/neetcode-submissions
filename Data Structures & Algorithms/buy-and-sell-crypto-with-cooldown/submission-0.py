class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i,canBuy) in dp:
                return dp[(i, canBuy)]
            coolDown = dfs(i+1, canBuy)
            if canBuy:
                buycase = dfs(i+1, not canBuy) - prices[i]
                dp[(i,canBuy)] = max(buycase, coolDown)
            else:
                sellCase = dfs(i+2, not canBuy) + prices[i]
                dp[(i,canBuy)] = max(sellCase, coolDown)

            return dp[(i,canBuy)]

        return dfs(0, True)
        