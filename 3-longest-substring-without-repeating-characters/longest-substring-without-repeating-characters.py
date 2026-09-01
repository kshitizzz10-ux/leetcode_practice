class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ss = set()
        ml = 0
        while r < len(s):
            if s[r] not in ss:
                ss.add(s[r])
                ml = max(ml,len(ss))
                r += 1
            else:
                ss.discard(s[l])
                l += 1
        return ml