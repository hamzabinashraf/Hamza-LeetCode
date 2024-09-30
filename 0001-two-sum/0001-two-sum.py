class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range (len(nums)):
            value = target - nums[i]
            if value in dict:
                return dict[value],i
            dict[nums[i]] = i