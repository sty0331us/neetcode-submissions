class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one_step_back = 2
        two_step_back = 1

        for i in range(3, n+1):
            cur = one_step_back + two_step_back
            two_step_back = one_step_back
            one_step_back = cur

        return one_step_back
        