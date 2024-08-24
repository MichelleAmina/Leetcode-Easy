"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

def searchInsert(nums, target):
    # if target in nums:
    #     return nums.index(target)
    # else:
    #     for i in range(len(nums)):
    #         if nums[i] > target:
    #             return i 
    #     return len(nums)
    con = 0
    for i in nums:
        if(target == i):
            return con
        elif(target < i):
            return con
        con += 1
    return con

print(searchInsert([1,3,5,6], 5)) # 2
print(searchInsert([1,3,5,6], 2)) # 1
print(searchInsert([1,3,5,6], 7)) # 4