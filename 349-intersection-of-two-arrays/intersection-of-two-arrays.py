class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        snums1 = set(nums1)
        snums2 = set(nums2)
        return list(snums1.intersection(snums2))
        
        