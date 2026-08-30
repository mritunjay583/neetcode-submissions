class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        overall_max = 0
        for i in range(len(prices)):
            temp_max = 0
            for j in range(i+1,len(prices)):
                temp_max = max(temp_max,prices[j]-prices[i])
            overall_max = max(overall_max,temp_max)
        
        return overall_max

        