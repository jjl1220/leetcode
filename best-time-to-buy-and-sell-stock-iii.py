class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices==[]: return 0
        forward=backward=[0 for i in prices]
        maxprofit=0
        low=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<low: low=prices[i]
            maxprofit=max(maxprofit,prices[i]-low)
            forward[i]=maxprofit
        maxprofit=0
        high=prices[-1]
        for i in reversed(range(len(prices))):
            if prices[i]>high: high=prices[i]
            maxprofit=max(maxprofit,high-prices[i])
            backward[i]= maxprofit
            if i>0: backward[i]+=forward[i-1]
        return max(backward)