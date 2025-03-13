# Using prefix and postfix product arrays 
# My solution
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pref = [1]*len(nums)
        postf = [1]*len(nums)
        temp = 1
        for i in range(len(nums)):
            if i!= 0:
                temp *= nums[i-1]
                pref[i] = temp
        
        temp = 1
        print(pref)
        for i in range(len(nums)-2, -1, -1):
            temp *= nums[i+1]
            postf[i] = temp   
        print(postf)

        res = []
        for i in range(len(nums)):
            res.append(postf[i] * pref[i])
        
        return res
        
# Neetcode solution
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)

        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]   
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res