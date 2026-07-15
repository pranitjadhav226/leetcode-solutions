class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        reversed_num = 0
        while num > 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num = num // 10
        if x < 0:
            reversed_num = -reversed_num
        
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num
        
