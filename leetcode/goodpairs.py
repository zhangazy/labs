class Solution:
answer = 0
i = 0
j = 1
    for i in range(len(nums)) :
        for j in range(len(nums)):
          if nums[i] == nums[j] and i < j:
            print(answer)

        
        
        
        
        