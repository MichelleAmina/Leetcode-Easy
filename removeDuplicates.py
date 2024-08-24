from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        j = 0

        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1 
        
        """
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
        """

        



solution = Solution()

print(solution.removeDuplicates([1,1,2]))  # [1,2,_] = 2
#print(solution.removeDuplicates([[0,0,1,1,1,2,2,3,3,4]]))  # [0,1,2,3,4,_,_,_,_,_] = 5