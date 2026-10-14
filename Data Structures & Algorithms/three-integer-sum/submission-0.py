class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = set()
        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            while j < k:
                triplet_sum = nums[i] + nums[j] + nums[k]
                if triplet_sum == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif triplet_sum > 0:
                    k -= 1
                else:
                    j += 1
        return [list(value) for value in res]

