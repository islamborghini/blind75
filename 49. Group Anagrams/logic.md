# Solution for 49. Group Anagrams
## Logic behind my solution:
<p>Having a hashmap, every key is a sorted string and the value of this key is the list of anagrams. Return the values of a hashmap</p>
<p>Time complexity: O(n^2 log n) </p>
<p>Space complexity: O(n)</p>

## Logic behind Greg Hogg's solution:
<p>Having a hashmap, every key is a tuple of frequencies of ASCII characters. For each tuple key we add a string.</p>
<p>Time complexity: O(n * m)</p>
<p>Space complexity: O(n * m)</p>