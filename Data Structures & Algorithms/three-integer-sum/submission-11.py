class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for index, a in enumerate(nums):
            if a > 0:
                break # positive numbers only can't sum up to 0
            if index > 0 and nums[index-1] == a:
                continue
            l,r = index+1,len(nums)-1
            while l < r:
                threeSum = nums[l]+a+nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l +=1
                else:
                    triplets.append([a,nums[l],nums[r]])
                    l +=1
                    r-=1
                    while l<r and nums[l-1]==nums[l]:
                        l +=1
        return triplets


        