class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT , countWindow = {},{}
        minLen , res = float("infinity"),[-1,-1]
        left = 0
        charsSatisfied = 0
        
        for c in t:
            countT[c] = 1+ countT.get(c,0)
        charsNeeded = len(countT)

        for right in range(len(s)):
            countWindow[s[right]] = 1 + countWindow.get(s[right],0)
            if s[right] in countT and countWindow[s[right]] == countT[s[right]]:
                charsSatisfied += 1
            while charsSatisfied == charsNeeded:  
                if (right - left +1) < minLen:
                    minLen = right - left + 1
                    res = [left,right]      
                # shrink the window to get the least size valid window
                countWindow[s[left]] -= 1
                if s[left] in countT and countWindow[s[left]] < countT[s[left]]:
                    charsSatisfied -= 1
                left +=1
        left,right = res
        return s[left:right+1] if minLen != float("infinity") else ""