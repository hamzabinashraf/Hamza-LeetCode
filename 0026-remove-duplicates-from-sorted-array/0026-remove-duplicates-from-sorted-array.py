class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)-1
        while k>= 1:
            if nums[k] == nums[k-1]:
                nums.pop(k)
            k-=1
        return len(nums)