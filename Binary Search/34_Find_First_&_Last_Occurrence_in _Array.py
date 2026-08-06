class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def LB():
            n = len(nums)
            low = 0 
            high = n-1
            ans = n
            while low <= high :
                mid = (low + high) // 2 
                if nums[mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1 
            return ans 
        def UB():
            n = len(nums)
            low = 0 
            high = n-1
            ans = n
            while low <= high :
                mid = (low + high) // 2 
                if nums[mid] > target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1 
            return ans                
        first = LB()
        last = UB() - 1

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        return [first, last]
