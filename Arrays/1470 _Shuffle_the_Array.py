class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m = len(nums)
        mid = m // 2
        i = 0 
        j = mid 
        result = []
        while j < m :
            result.append(nums[i])
            i += 1
            result.append(nums[j])
            j += 1
        return result            
