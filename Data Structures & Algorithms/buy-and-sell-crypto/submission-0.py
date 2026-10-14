class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0

        for j in range(1, len(prices)):
            while i <j and prices[j] < prices[i]:
                i += 1
            max_profit = max(max_profit, prices[j]-prices[i])
        return max_profit