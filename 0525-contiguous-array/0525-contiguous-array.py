class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_value = 0
        max_value = 0
        for i,num in enumerate(nums):
            sum_value += 1 if num == 1 else -1
            if sum_value == 0:
                max_value = i+1
            elif sum_value in mp:
                max_value = max(max_value,i-mp[sum_value])
            else:
                mp[sum_value] = i
        return max_value