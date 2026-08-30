class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_array = [0]*len(prices)
        temp_max = 0
        for i in range(len(prices)-2,-1,-1):
            temp_max = max(temp_max,prices[i+1])
            max_array[i] = temp_max - prices[i]
            
        return max(max_array)
        