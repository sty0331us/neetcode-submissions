class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getDigitSum(n)

        return n == 1

    def getDigitSum(self, num: int) -> int:
            res = num
            sum =0

            while res > 0:
                sum += (res%10)**2
                res //= 10

            return sum
        