# from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        # seen_element = defaultdict(int)
        # for x in nums:
        #     seen_element[x] += 1
        #     if seen_element[x] > 1:
        #         return True

        for i,j in enumerate(nums):
            if i+1 < len(nums):
                if nums[i]==nums[i+1]:
                    return True
        return False

        