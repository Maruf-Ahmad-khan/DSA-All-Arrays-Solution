from typing import List
class Solution:
     def Longest_Consecutive_Sequence(self, nums : List[int])->int:
          numSet = set(nums)
          longest = 0
          for n in nums:
               if(n - 1) not in numSet:
                    length = 0
               while(n + length) in numSet:
                    length += 1
               longest = max(length, longest)
          return longest
     
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
     
sol = Solution()
nums = [100,4,200,1,3,2]
ans = sol.Longest_Consecutive_Sequence(nums)
print("Longest Consecutive sequence is : ")
print(ans)
          