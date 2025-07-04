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