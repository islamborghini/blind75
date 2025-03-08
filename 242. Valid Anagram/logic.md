## 1st method - sorted strings
<p>Simply compare two sorted strings. However, slow as it requires sorting</p>
<p>Time Complexity: O(nlogn)</p>
<p>Space Complexity: O(1)</p>

## 2nd method - hashmaps
<p>Create a counter that checks the number of appearances of every element in the string using a hashmap. Do that for both strings. Then compare two hashmaps</p>
<p>Time Complexity: O(n)</p>
<p>Space Complexity: O(n)</p>