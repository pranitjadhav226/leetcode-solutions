class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = 0
        max_count = float("-inf")
        for i in range(len(nums)):
            count = count + nums[i]
        
            if count > max_count:
                max_count = count
            
            if count < 0 :
                count = 0
            
        return max_count    
        
