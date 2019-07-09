
class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            differ = prices[i+1] - prices[i]
            if differ > 0:
                profit += differ
        return profit