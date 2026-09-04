from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        r = 0
        pfreq = Counter(p)
        sfreq = {}
        result = []

        for r in range(len(s)):
            sfreq[s[r]] = sfreq.get(s[r], 0) + 1
            
            if r-l+1 == len(p) :
                if sfreq == pfreq:
                    result.append(l)
                sfreq[s[l]] -= 1
                if sfreq[s[l]] == 0:
                    del sfreq[s[l]]
         
                l += 1
        return result
            
                
                