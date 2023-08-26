class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
             hashmap[num] = hashmap.get(num, 0) + 1
        
        return sorted(hashmap, reverse=True, key=lambda x: hashmap[x])[:k]