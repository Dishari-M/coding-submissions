class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num-1) not in numSet:
                sequenceLen = 0
                while (num + sequenceLen) in numSet:
                    sequenceLen +=1
            
                longest = max(longest,sequenceLen)
        return longest

        