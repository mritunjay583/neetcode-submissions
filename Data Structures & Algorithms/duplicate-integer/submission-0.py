from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_element = defaultdict(int)
        for x in nums:
            seen_element[x] += 1
            if seen_element[x] > 1:
                return True

        return False

        