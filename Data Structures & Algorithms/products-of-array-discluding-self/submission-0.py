class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = []
        ans1 = 1
        pre.append(ans1)
        for i in range(len(nums)-1):
            ans1 = ans1*nums[i]
            pre.append(ans1)
        
        post = [1]*len(nums)
        ans2 = 1
        for i in range(len(nums)-1,-1,-1):
            post[i]=post[i]*ans2
            ans2 = ans2*nums[i]
        
        ans = []
        for i in range(len(nums)):
            ans.append(pre[i]*post[i])
    
        return ans