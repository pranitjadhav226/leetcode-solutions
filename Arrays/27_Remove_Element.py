class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j

# LeetCode 27 - Remove Element
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
        
