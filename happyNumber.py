"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which 
does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false
 
Constraints:
1 <= n <= 231 - 1
"""


def isHappy(n):
    # n_str = str(n)

    # output = []
    
    # for char in n_str:
    #     output.append(int(char))

    # return output

    # return list(map(int, str(n)))


    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(char) ** 2 for char in str(n))

    return n == 1


    


print(isHappy(19)) # True
print(isHappy(2)) # False 


"""
1. Initialization of sum:
You should initialize sum for each iteration of processing the digits of the number. If sum is initialized 
only once, it will keep accumulating values indefinitely, which is not what we want.

2. Checking for a Cycle:
To handle numbers that enter a cycle and never reach 1, you should use a set to keep track of the numbers 
you've seen before. If you encounter a number that you've already processed, you can conclude that the number 
is not happy.

3. Main Loop:
The main loop should iterate while the number is not equal to 1 and hasn't been seen before.

4. Correct Summing of Digits:
You need to correctly sum the squares of the digits and then reassign this sum to n for the next iteration.

"""