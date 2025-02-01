class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if right==0:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[right]!=nums[right-1]:
            return nums[right]


        while(left<=right):
            mid=(left+right)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            
            if (mid%2==0 and nums[mid+1]==nums[mid]) or (mid%2==1 and nums[mid]==nums[mid-1]):
                left=mid+1
            else:
                right=mid-1