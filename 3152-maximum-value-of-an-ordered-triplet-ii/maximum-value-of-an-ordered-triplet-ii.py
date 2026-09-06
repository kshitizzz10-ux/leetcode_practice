class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_before = nums[0]
        min_before = nums[0]
        max_diff = float("-inf")
        min_diff = float("inf")
        ans = float("-inf")
        
        for j in range(1,len(nums)-1):
            max_diff = max(max_diff,max_before - nums[j])
            min_diff = min(min_diff,min_before - nums[j])
            k = j+1
            if nums[k] >= 0:
                ans = max(ans,max_diff*nums[k])
            else:
                ans = max(ans,min_diff*nums[k])

            max_before = max(max_before , nums[j])
            min_before = min(min_before,nums[j])
        
        if ans > 0:
            return ans
        else:
            return 0
            
            
        
            