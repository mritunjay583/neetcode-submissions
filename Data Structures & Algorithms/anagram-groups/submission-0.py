from collections import defaultdict as dd
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dd(list)
        for x in strs:
            hash_map[",".join(sorted(x))].append(x)
        
        final_list = []
        for x in hash_map.values():
            final_list.append(x)
        return final_list