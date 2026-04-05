class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.getMax(nums[:-1]), self.getMax(nums[1:]))

    def getMax(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            newMax = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = newMax
        return rob2