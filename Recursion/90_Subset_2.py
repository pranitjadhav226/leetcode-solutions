class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def func(index, subset):
            result.append(subset.copy())

            for i in range(index, len(nums)):

                if i > index and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                func(i + 1, subset)
                subset.pop()

        func(0, [])
        return result
