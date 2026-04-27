class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums)//2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            newDP = set()
            for n in dp:
                if n + nums[i] == target:
                    return True
                
                if n + nums[i] < target:
                    newDP.add(n + nums[i])
                newDP.add(n)
            dp = newDP
        return False