"""
476. Number Complement
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's 
in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. 
So you need to output 2.

Example 2:
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. 
So you need to output 0.
 

Constraints:
1 <= num < 231
"""

def findComplement(num):
    # if num >= 1:
    #     binary = bin(num).replace("0b", "") 

    #     complement_bin = ''

    #     for bit in binary:
    #         if bit == '1':
    #             complement_bin += '0'  
    #         else:
    #             complement_bin += '1'  

       
    #     return int(complement_bin, 2)
    
    # else:
    #     return 0

    # num = bin(num)[2:]
    # compliment = ""
    # for bit in num:
    #     if bit == "0": compliment+="1"
    #     else: compliment+="0"
    # return int(compliment, 2)

    binary = bin(num)[2:]
    complement = ''.join('1' if bit == '0' else '0' for bit in binary)

    return int(complement, 2)

print(findComplement(5))
print(findComplement(1))