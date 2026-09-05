class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = float("inf")
        for i in range(len(arr)-1):
            diff = min(diff,abs(arr[i]-arr[i+1]))
        result = []
        
        for i in range(len(arr)-1):
            res = []
            if abs(arr[i]-arr[i+1]) == diff:
                res = [arr[i],arr[i+1]]
                result.append(res)
        return result
