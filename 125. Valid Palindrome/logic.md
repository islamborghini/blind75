# Solution for 125. Valid Palindrome
## Solution using two pointers
<p>Set a left pointer to position 0 and R to the last position. Run the while loop until L is smaller than R. For both pointers, if the character is not alphanumerical, move the pointer towards the center of the string. Else, check whether left pointer character is the same as right pointer character</p>