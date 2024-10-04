class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {'(':')','[':']','{':'}'}

        for c in s:
            if c in bracket:
                stack.append(c)
            elif not stack or bracket[stack.pop()] != c:
                return False
        return not stack