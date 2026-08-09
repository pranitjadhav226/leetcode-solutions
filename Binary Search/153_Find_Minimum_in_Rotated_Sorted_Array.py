class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0 
        high = n-1
        mini = float("inf")
        while low <= high :
            mid = (low + high ) // 2
            if nums[mid] <= nums[high] :
                if nums[mid] < mini:
                    mini = nums[mid]
                high = mid - 1
            else :
                if nums[low] < mini:
                    mini = nums[low]
                low = mid + 1
        return mini
                
            
        
