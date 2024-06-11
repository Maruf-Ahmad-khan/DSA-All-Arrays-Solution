class Solution:
     def Majority_Element(self, arrs:int)->int:
          count = 0
          ele = None
          for arr in arrs:
               if count == 0:
                    count = 1
                    ele = arr
               elif arr == ele:
                    count += 1
               else:
                    count -= 1
          count_1 = 0
          for arr in arrs:
               if arr == ele:
                    count_1 += 1
          
          if count_1 > (len(arrs)// 2) :
               return ele 
          return - 1        

sol = Solution()                        
arrs = [2, 2, 1, 1, 1, 2, 2]                   
ans = sol.Majority_Element(arrs)
print(ans)