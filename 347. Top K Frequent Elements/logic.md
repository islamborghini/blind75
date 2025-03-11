# Solution for 347. Top K Frequent Elements:
## Solution using a Counter and a Heap:
<p>By using a counter, we can have a minheap. If the heap length is smaller than k, push the elements to the minheap one-by-one in the format: (frequency, key). Else: do the heappushpop of the element. After that, return all the elements of the keys (h1) in the heap. </p>
<p>Time complexity: O(n log k)</p>
<p>Space complexity: O(n)</p>

## Solution using a Counter and a Bcket Sort:
<p>We can use a counter to calculate the frequencies. Then we can have an array, where the index is the frequency of the certain element and the value is an array of elements with that frequency. Then, we simply return the k non-zero values from right to left of the array</p>
<p>Time complexity: O(n)</p>
<p>Space complexity: O(n)</p>
