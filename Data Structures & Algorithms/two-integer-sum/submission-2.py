class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in seen_dict:
                return [seen_dict[res],i]
            seen_dict[num] = i

      