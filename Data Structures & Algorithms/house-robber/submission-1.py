class Solution:
    def rob(self, nums: List[int]) -> int:
        num = len(nums)
        cache=[-1]*num
        def dfs(houseNum):
            if houseNum >= num:
                return 0
            if cache[houseNum]!= -1:
                return cache[houseNum]
            cache[houseNum] = max(nums[houseNum] + dfs(houseNum+2),dfs(houseNum+1))
            return cache[houseNum]
        return dfs(0)
            
        