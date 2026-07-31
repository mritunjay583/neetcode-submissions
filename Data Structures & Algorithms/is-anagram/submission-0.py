from collections import defaultdict as dd
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = dd(int)
        for x in s:
            hashMap[x]+=1
        
        for x in t:
            if x not in hashMap:
                return False
            else:
                hashMap[x]-=1
        
        for x in hashMap.values():
            if x != 0:
                return False
        
        return True