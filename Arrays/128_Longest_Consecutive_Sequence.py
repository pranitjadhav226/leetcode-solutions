class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        for i in range (0 , len(nums)):
            my_set.add(nums[i])

        largest = 0 

        for num in my_set :
            if num - 1 not in my_set :
                count = 1 
                x = num 
                while x + 1 in my_set :
                    count += 1 
                    x += 1 
                largest = max(largest , count)
        return largest                
        
