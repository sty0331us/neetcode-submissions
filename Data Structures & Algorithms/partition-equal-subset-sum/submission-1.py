class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False

        target = total//2
        bit = 1

        for n in nums:
            bit |= (bit<<n)

        return True if (bit >> target) & 1 else False