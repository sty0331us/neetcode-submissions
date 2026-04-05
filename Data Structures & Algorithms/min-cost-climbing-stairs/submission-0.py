class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step_back = 0
        two_step_back = 0

        for i in range(len(cost)-1,-1,-1):
            cur = cost[i] + min(one_step_back, two_step_back)
            two_step_back = one_step_back
            one_step_back = cur

        return min(one_step_back, two_step_back)
        