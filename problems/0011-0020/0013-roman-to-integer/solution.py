"""
Success
Details
Runtime: 44 ms, faster than 73.62% of Python3 online submissions for Roman to Integer.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        minus_dict = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M'],
        }

        sum = 0

        for idx, symbol in enumerate(s):
            sign = 1
            if symbol in minus_dict and (idx + 1) < len(s):
                if s[idx + 1] in minus_dict[symbol]:
                    sign = -1
            sum += sign * roman_dict[symbol]

        return sum
