class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        if len(nums)<=1:
            return len(nums)
        nums.sort()
        temp_arr = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]-1:
                    temp_arr[i] = temp_arr[j] + 1
                    break
        return max(temp_arr)