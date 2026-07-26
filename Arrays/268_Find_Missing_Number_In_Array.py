class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_map = {}

        for num in nums:
            hash_map[num] = 1

        for i in range(len(nums) + 1):
            if i not in hash_map:
                return i
        
