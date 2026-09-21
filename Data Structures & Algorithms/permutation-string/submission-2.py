class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        i=0
        temp_str = ('').join(sorted(s1))
        while True:
            if i+len(s1) > len(s2):
                return False
            part = ('').join(sorted(s2[i:i+len(s1)]))
            if temp_str == part:
                return True
            i = i+1
        
        return False

