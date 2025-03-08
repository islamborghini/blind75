# Solution by comparing two sorted strings
class Solution(object):
    def isAnagram(self, s, t):
        return True if sorted(s) == sorted(t) else False

# Solution by using hash table 
from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        h = defaultdict(int)
        h2 = defaultdict(int)
        for i in range(len(s)): 
            h[s[i]]+=1
        for j in range(len(t)):
            h2[t[j]]+=1
        print(h, h2)
        if h == h2:
            return True
        return False