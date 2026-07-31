from collections import defaultdict as dd
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = dd(int)
        for x in nums:
            hash_map[x]+=1
        
        sorted_dict = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        final_data = []
        for i, (key,value) in enumerate(sorted_dict.items()):
            if k==0:
                break
            final_data.append(key)
            k-=1

        return final_data