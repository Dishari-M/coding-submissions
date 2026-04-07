class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChars = {}
        longest = 0
        left = 0
        for index,ch in enumerate(s):
            if ch in uniqueChars:
                left = max(left,uniqueChars[ch]+1)
                
            uniqueChars[ch]=index
            longest = max(longest,index-left+1)


        return longest
        