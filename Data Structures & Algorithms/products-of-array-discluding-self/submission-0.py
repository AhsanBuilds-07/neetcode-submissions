from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         n = len(nums)
         output = [1] * n

        # First loop: Calculate prefix products
         prefix = 1

         for i in range(n):
            output[i] = prefix
            prefix = prefix * nums[i]

        # Second loop: Calculate suffix products
         suffix = 1

         for i in range(n - 1, -1, -1):
            output[i] = output[i] * suffix
            suffix = suffix * nums[i]

         return output