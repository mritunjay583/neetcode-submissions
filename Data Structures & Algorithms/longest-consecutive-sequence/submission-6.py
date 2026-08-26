class Solution:

    def longestConsecutive(self, nums: List[int]) -> int: 
        if len(nums)<=1:
            return len(nums)
        
        dp = {}
        elements_set = set()
        for i in nums:
            elements_set.add(i)
        
        for i in nums:
            cnt = 1
            j = i
            while(True):
                j = j+1

                if j not in elements_set:
                    break

                if j in dp:
                    cnt = cnt+dp[j]
                    break
                cnt+=1
            dp[i] = cnt

        return max(dp.values())