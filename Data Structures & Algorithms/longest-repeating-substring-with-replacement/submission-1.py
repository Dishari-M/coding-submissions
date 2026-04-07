class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = {}
        maxLen = 0
        l =0
        countMap[s[l]]=1
        maxFreq = 0
        for r in range(1,len(s)):
            countMap[s[r]]=countMap.get(s[r],0)+1
            maxFreq = max(maxFreq, countMap[s[r]])
            while (r-l+1)- maxFreq > k:
                countMap[s[l]] -=1
                l +=1
    
            maxLen = max(maxLen,(r-l+1))
        return maxLen

        