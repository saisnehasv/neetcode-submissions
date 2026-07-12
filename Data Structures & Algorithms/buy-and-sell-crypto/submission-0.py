class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0 
        buy = prices[0]
        for sell in prices[1:]:
            
            if sell <= buy:
                buy = sell
                continue
            
            profit = sell - buy
            maxprofit = max(profit,maxprofit)
        return maxprofit

        