class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed_num = 0
        num = x
        while num > 0:
            LD = num % 10
            reversed_num = reversed_num * 10 + LD
            num = num // 10
        return reversed_num == original
