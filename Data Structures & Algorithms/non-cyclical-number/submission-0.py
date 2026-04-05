class Solution:
    def isHappy(self, n: int) -> bool:

        def getDigitSum(num: int) -> int:
            res = num
            sum =0

            while res > 0:
                sum += (res%10)**2
                res //= 10

            return sum

        slow = n
        fast = getDigitSum(n)

        while fast != 1 and slow != fast:
            slow = getDigitSum(slow)
            fast = getDigitSum(getDigitSum(fast))

        return fast == 1
        