class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pfx = [0]*len(nums)
        sfx = [0]*len(nums)
        pfx[0] = nums[0]
        for i in range(1,len(nums)):
            pfx[i] = max(pfx[i-1],nums[i])
        sfx[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            sfx[i] = min(sfx[i+1],nums[i])
        diff = [0]*len(nums)
        for i in range(len(nums)):
            diff[i] = pfx[i]-sfx[i]
        for i in range(len(diff)):
            if diff[i] <= k:
                return i
                break
            
        return -1

