# Solution for 238. Product of Array Except Self
## Using postfix and prefix:
<p>We can run 2 loops. In these two loops we can have a temporary variable temp. We run through the first loop and multiply temp by every i-1 element. We run through the second loop and multiply temp by every i+1 element (from right to left). Then we can compute the product by: product[i] =  postfix[i] * prefix[i]</p> 
<p>Time complexity: O(n)</p>
<p>Space complexity: O(n)</p>