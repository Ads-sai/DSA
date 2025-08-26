class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        a=[]
        for i in range(n):
            for j in range(n-1,i,-1):
                if nums[i]+nums[j]==target:
                    a.append(i)
                    a.append(j)
        return a