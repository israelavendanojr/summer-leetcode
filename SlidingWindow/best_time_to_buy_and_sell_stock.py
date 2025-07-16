class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        max_p = 0

        while r in range(len(prices)-1):
            
            if prices[l] < prices[r]:
                r += 1
            else:
                l = r
                r += 1

            p = prices[r] - prices[l]
            max_p = max(p,max_p)

        
        return max_p

# REDO : 7/15/2025

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time : 3:06
        l = 0
        max_profit = float('-inf')

        for r in range(len(prices)):
            cur_profit = prices[r] - prices[l]

            if prices[r] < prices[l]:
                l = r

            max_profit = max(max_profit, cur_profit)

        return max_profit


# REDO : 7/16/2025

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time : 1:17
        max_p = 0

        l = 0
        for r in range(len(prices)):
            p = prices[r] - prices[l]
            max_p = max(max_p, p)

            if prices[r] < prices[l]:
                l = r

        return max_p