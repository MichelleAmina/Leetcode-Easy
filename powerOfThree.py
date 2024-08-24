"""
326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true
Explanation: 27 = 33

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1)
"""


def powerOfThree(n):
    if n <= 0:
        return False
    
    while n % 3 == 0:
        n //= 3

    return n == 1

print(powerOfThree(27)) # True
print(powerOfThree(0)) # False
print(powerOfThree(-1)) # False


"""
Explanation:
Step 1: Check if n is greater than 0. If it's not, return False since a power of three cannot be zero or 
negative.
Step 2: Use a loop to divide n by 3 as long as it is divisible by 3.
Step 3: After the loop, check if the final value of n is 1. If it is, then n is a power of three.

The line n //= 3 is a shorthand way of writing n = n // 3. It performs integer division on n by 3 and then 
updates n with the result.

Breaking Down n //= 3
Before the operation: n holds its current value.
During the operation: Python calculates the result of n divided by 3, rounding down if necessary.
After the operation: n is updated with the result of this division.


"""