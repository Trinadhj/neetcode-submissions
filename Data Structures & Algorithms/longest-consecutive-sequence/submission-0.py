class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        for i in nums:
            if i-1 not in set(nums):
                count = 1
                while i+1 in set(nums):
                    count += 1
                    i += 1
                longest = max(longest, count)
        return longest