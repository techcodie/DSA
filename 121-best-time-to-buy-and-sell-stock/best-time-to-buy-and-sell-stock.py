class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        maxp=0
        for i in range(len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            else:
                maxp=max(maxp,prices[i]-buy)
        return maxp