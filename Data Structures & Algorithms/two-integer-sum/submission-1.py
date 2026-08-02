class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j];
        prevmap = {}
        for i , n in enumerate(nums):
            if (target - n) in prevmap:
                return [prevmap[target-n],i]
            prevmap[n] = i