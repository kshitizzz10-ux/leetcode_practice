from collections import deque
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        dqnums = deque(nums)
        dqnums.rotate(k)
        nums[:] = dqnums


        