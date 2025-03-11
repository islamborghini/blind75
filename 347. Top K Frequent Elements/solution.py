#Solution using counter + heap 
from collections import defaultdict, Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        heap = []
        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [h[1] for h in heap]
    
#Solution using counter + bucket sort
from collections import defaultdict, Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        n = len(nums)
        buckets = [0] * (n+1)
        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else: 
                buckets[freq].append(num)

        ret = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break            
        return ret
