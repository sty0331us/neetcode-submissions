class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_max = nums[0]
        final_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            final_max = max(current_max, final_max)

        return final_max
        