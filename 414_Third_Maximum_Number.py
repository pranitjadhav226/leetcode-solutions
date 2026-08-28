class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        n = len(nums)
        i = n-1
        if n < 3 :
            return nums[i]
        else : 
            return nums[i-2]    
        
