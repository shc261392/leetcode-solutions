"""
Success
Details
Runtime: 48 ms, faster than 79.33% of Python3 online submissions for Two Sum.
Memory Usage: 14.1 MB, less than 62.09% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            if (target - num) in nums_dict:
                return [
                    nums_dict[target - num],
                    idx,
                ]
            nums_dict[num] = idx
