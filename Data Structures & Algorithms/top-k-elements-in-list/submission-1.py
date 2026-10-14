class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        nums_counter = Counter(nums)

        sorted_nums_counter = sorted(nums_counter.items(), key = lambda x : x[1], reverse =True)

        return [k for k,v in sorted_nums_counter][:k]