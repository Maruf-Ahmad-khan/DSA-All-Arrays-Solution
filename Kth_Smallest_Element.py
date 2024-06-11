# Input:
# n = 6
# arr[] = 7 10 4 3 20 15
# k = 3
# l=0 r=5

# Output : 
# 7

# Explanation :
# 3rd smallest element in the given 
# array is 7.

class Solution:
     def KthSmallest(self, arr:int, r:int, l:int, k:int)->int:
          # Create an empty list
          ans = []
          # iterate over the array
          for i in range(l, r + 1):
               # append the elements into the empty list
               ans.append(arr[i])
          # sort the array ans = [3, 4, 7, 10, 15, 20]
          ans.sort() 
          # return the index which is present in the ans array    
          return ans[k - 1]
     
ans = Solution()
arr = [7, 10, 4, 3, 20, 15]
k = 3
l = 0
r = 5
ans = ans.KthSmallest(arr, r , l, k)
print("The Kth smallest Element is : ")
print(ans)
     