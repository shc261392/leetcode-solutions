"""
Success
Details
Runtime: 56 ms, faster than 77.02% of Python3 online submissions for Palindrome Number.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
"""

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)

        if len(s) <= 1:
            return True

        mid_idx = len(s)/2
        left = s[:math.ceil(mid_idx)]
        right = s[:math.floor(mid_idx)-1:-1]
        return (left == right)
