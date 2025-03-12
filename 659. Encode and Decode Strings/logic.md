# Solution for 659. Encode and Decode Strings
## Solution with simple string operations
<p>To encode the word, we need to:<br>
    Create one long string in the format of: <br>
    ni#wordi,<br>
    where ni - integer, representing the length of the word added, <br>
    # - a symbol to differentiate the separate words, symbolizes a beginning of a word,<br>
    wordi - word from the given string array<br><br>
    In order to decode the word we simply find for a '#', knowing integer before is the length of the word. Then, we simply add a string of length elements starting from the "#". 
</p>


