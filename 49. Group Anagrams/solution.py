
#My solution using hashmaps
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = defaultdict(list)
        for st in strs:
            sorted_st = ''.join(sorted(st))
            h[sorted_st].append(st)
        
        return list(h.values())

#Greg Hogg's solution using hashmaps
class Solution:
    def groupAnagrams(self, strs):
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)
            
        return list(anagrams_dict.values())


        