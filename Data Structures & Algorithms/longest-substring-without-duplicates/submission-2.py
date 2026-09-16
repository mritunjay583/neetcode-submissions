class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        left = 0
        v= set()
        v.add(s[left])
        right = left+1

        max_len = 1

        while True:
            if right>=len(s):
                break
            if s[right] not in v:
                v.add(s[right])
                right = right+1
                max_len = max(max_len,right-left)
            else:
                while s[left] != s[right]:
                    v.remove(s[left])
                    left+=1
                max_len = max(max_len,right-left)
                left = left+1
                right = right+1

        return max_len