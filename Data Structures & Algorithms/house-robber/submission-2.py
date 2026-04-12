class Solution:
    def rob(self, nums: List[int]) -> int:
        num = len(nums)
        if num == 0:
            return 0
        if num == 1:
            return nums[0]
        dp = [0]*num
        dp[0]= nums[0]
        dp[1] = max(nums[0],nums[1])
        for houseNum in range(2,num):
            dp[houseNum] = max(nums[houseNum]+ dp[houseNum-2], dp[houseNum-1])
        return dp[-1]
            
        