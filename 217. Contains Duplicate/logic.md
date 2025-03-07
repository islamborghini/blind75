# Solution for 217. Contains Duplicate
## 1st Method - using dictionaries: 
<p>For every number in the array, you check whether it is in a dictionary, if it is not, you increase it's count. If it is in the dictionary, you return True as we have a duplicate. If there are no duplicates, just return False</p>

## 2nd Method - using hashsets: 
<p>Similarly as in a dictionary solution, for every number in the array check if it is in a hashset. If it is not, add it to the hashet. If it is already there, return True as we have a duplicate. Otherwise, if there were no duplicates return False</p>