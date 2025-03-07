# Solution using dictionaries: 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = defaultdict(int)
        for num in nums: 
            if num not in d:
                d[num] += 1
            else:
                return True
        
        return False

# Solution using sets: 
class Solution(object):
    def containsDuplicate(self, nums):
        d =  set()
        for num in nums:
            if num not in d:
                d.add(num)
            else:
                return True
        return False