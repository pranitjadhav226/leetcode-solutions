class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range (n-1):
            if nums[i+1] - nums[i] != 1 :
                current = nums[i] + 1
                while current < nums[i+1]:
                    result.append(current)
                    current += 1

        return result
        
