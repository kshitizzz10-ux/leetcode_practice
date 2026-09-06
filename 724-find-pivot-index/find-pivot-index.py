class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for num in nums:
            total += num
        left = 0
        for i in range(n):
            left += nums[i]
            right = total - left 
            if (left - nums[i]) == right:
                return i 
                break
        return -1


