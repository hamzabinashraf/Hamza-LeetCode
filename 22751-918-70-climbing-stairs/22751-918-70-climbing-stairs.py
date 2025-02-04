class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        first = 1
        second = 2
        for i in range(n-2):
            temp = first + second
            first = second
            second = temp
        return second