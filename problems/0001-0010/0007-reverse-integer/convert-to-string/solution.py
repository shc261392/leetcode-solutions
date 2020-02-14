"""
Success
Details
Runtime: 24 ms, faster than 93.90% of Python3 online submissions for Reverse Integer.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
This solution is very easy for Python
"""
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        s = str(abs(x))[::-1]
        result = sign * int(s)
        if result > 2147483647 or result < -2147483648:
            return 0
        else:
            return result
