class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        missing_value = 1
        while missing_value in num_set:
            missing_value += 1
        return missing_value