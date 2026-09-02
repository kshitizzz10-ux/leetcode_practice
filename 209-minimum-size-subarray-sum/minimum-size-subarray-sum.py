class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        ml = float('inf')
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                ml = min(r-l+1,ml)
                sum -= nums[l]
                l += 1
        if ml == float('inf') :
            return 0
        else :
            return ml



            