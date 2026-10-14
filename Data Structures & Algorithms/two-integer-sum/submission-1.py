class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in index_dict:
                return [index_dict[res],i]
            index_dict[nums[i]] = i
        return None