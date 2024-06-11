from typing import List
class Solution:
     def Set_Matrix_Zero(self, matrix: List[List[int]])->None:
          rows = len(matrix)
          cols = len(matrix[0])
          zero_rows = set()
          zero_cols = set()
          for i in range(rows):
               for j in range(cols):
                    if matrix[i][j] == 0:
                         zero_rows.add(i)
                         zero_cols.add(j)
          
          for i in range(rows):
               for j in range(cols):
                    if i in zero_rows or j in zero_cols:
                         matrix[i][j] = 0

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]] 
sol = Solution()                        
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.Set_Matrix_Zero(matrix)
print("The zero matrix is : ")
for row in matrix:
     print(row)

                         
                    
          