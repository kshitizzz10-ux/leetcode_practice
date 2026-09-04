class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi = 0
        diffs = []
        for i in range(len(nums)):
            mini = float('inf')
            maxi = max(maxi,nums[i])
            j = i
            while j < len(nums):
                
                mini = min(mini,nums[j])
                j += 1
            diff = maxi - mini
            diffs.append(diff)
        for i in range(len(diffs)):
            if diffs[i] <= k:
                return i
                break
            else:
                continue
        return -1
