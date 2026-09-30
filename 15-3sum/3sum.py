class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1
            while left < right:
                if (nums[i] + nums[left] + nums[right]) < 0:
                    left += 1
                elif (nums[i] + nums[left] + nums[right]) > 0:
                    right -= 1
                else:
                    result.add((nums[i],nums[left],nums[right]))
                    right -= 1
                    left += 1
        triplets = [list(t) for t in result]
        
        return triplets
            
        
                    
                





