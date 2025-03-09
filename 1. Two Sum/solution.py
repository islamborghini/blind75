# Solution using hashmaps
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = defaultdict()
        for i, num in enumerate(nums):
            if num not in h:
                h[target - num] = i
            else:
                return [i, h[num]]
                
