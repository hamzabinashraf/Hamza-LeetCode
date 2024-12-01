class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = ans = maxJump = 0
        
        while r < len(nums) - 1:  
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            ans += 1
        return ans