class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if mid % 2 == 0:
                partner = nums[mid + 1]
            else:
                partner = nums[mid - 1]

            if nums[mid] == partner:
                low = mid + 1
            else:
                high = mid

        return nums[low]
