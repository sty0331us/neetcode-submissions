class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in prev:
                return [prev[complement], i]
            prev[num] = i

        return []