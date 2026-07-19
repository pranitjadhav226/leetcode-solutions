class Solution:
    def reverseString(self, s: List[str]) -> None:

        def fun(left, right):
            if left >= right:
                return

            s[left], s[right] = s[right], s[left]
            fun(left + 1, right - 1)

        fun(0, len(s) - 1)
