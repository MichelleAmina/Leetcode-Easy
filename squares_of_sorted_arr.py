def sorted_squares(nums):
    squared_nums = [num**2 for num in nums]
    squared_nums.sort()
    return squared_nums

print(sorted_squares([-7,-3,2,3,11]))