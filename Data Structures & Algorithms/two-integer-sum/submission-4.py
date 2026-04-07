class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,n in enumerate(nums):
            diff = target - n
            if diff in nums:
                index2 =  nums.index(diff)
                if index != index2:
                    if index > index2:
                        return [index2,index]
                    else:
                        return [index,index2]
        