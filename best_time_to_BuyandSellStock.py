class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min =9999999999999
        profit=0
        for i in range(0,len(prices)):
            if prices[i]<min:
                min=prices[i]
            if prices[i]-min>profit:
                profit=prices[i]-min
        return profit
