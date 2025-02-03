class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        Inc = Dec = max_length = 1
        for i in range (len (nums) - 1):
            if nums[i]>nums[i+1]:
                Inc = 1
                Dec +=1
            elif nums[i]<nums[i+1]:
                Inc +=1
                Dec = 1
            else:
                Inc = 1
                Dec = 1
            max_length = max(max_length, Inc, Dec)
        return max_length
