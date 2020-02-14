"""
Success
Details
Runtime: 136 ms, faster than 47.65% of Python3 online submissions for Container With Most Water.
Memory Usage: 14.6 MB, less than 11.58% of Python3 online submissions for Container With Most Water.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height) - 1

        while (start < end):
            area = (end - start) * min(height[start], height[end])
            max_area = max(max_area, area)
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1

        return max_area
