class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]* len(nums)
        right_prod = [1]* len(nums)
        final_prod = [1] * len(nums)

        for i in range(1,len(nums)):
            left_prod[i] = left_prod[i-1] * nums[i-1]
        print(left_prod)

        for j in range(len(nums)-2, -1, -1):
            right_prod[j] = right_prod[j+1] * nums[j+1]
        print(right_prod)

        for i in range(len(nums)):
            final_prod[i] = left_prod[i] * right_prod[i]
        
        return final_prod