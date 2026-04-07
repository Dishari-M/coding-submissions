class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        for l in range(len(nums)):
            r=l+1
            while r < len(nums):
                ele = -1*(nums[l]+nums[r])
                if  ele in nums:
                    third = nums.index(ele)
                    if third != l and third != r:
                        triplet = tuple(sorted((nums[l],nums[r],nums[third])))
                        if triplet not in triplets:
                            triplets.add(triplet)
                r+=1
        return list(triplets)
            




        