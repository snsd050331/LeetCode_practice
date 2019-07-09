
class Solution:
    def maxProfit(self, prices):
        if prices == []:
            return 0
        res = 0
        small = prices[0]
        for i in prices[1:]:
            small = min(i, small)
            if res < i - small:
                res = i - small
        return res