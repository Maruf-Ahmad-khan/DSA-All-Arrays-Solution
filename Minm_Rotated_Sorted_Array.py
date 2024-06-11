from typing import List
class Solution:
     def Minm_Rotated_Sorted_Array(self, nums:List[int])->int:
          low, high = 0, len(nums) - 1
          mini = float('inf')
          while low <= high:
               mid = low + (high - low) // 2
               if nums[low] <= nums[mid]:
                    mini = min(mini, nums[low])
                    low = mid + 1
               else:
                    mini = min(mini, nums[mid])
                    high = mid - 1
          return mini
sol = Solution()     
nums = [3,4,5,1,2]
ans = sol.Minm_Rotated_Sorted_Array(nums)
print("The minimum rotated sorted array is : ")
print(ans)