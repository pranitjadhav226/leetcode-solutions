class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def build(start, current, remaining):
            if remaining == 0:
                result.append(current)
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue
                build(i, current + [candidates[i]], remaining - candidates[i])

        build(0, [], target)
        return result
