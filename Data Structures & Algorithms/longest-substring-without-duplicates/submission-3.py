class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChars = set()
        longest = 0
        left = 0
        for index,ch in enumerate(s):
            while ch in uniqueChars:
                uniqueChars.remove(s[left])
                left +=1
                
            uniqueChars.add(ch)
            longest = max(longest,index-left+1)


        return longest
        