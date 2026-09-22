from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreq = {}
        for char in s:
            sfreq[char] = sfreq.get(char,0) + 1
        tfreq = {}
        for char in t:
            tfreq[char] = tfreq.get(char,0) + 1
        if sfreq == tfreq:
            return True
        return False

        