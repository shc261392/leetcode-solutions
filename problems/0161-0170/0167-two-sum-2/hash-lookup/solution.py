"""
Success
Details
Runtime: 56 ms, faster than 97.31% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.

It's exactly the same solution as 0001 hash-lookup
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_dict = {}
        for idx, number in enumerate(numbers):
            if (target - number) in numbers_dict:
                return [
                    numbers_dict[target - number] + 1,
                    idx + 1,
                ]
            numbers_dict[number] = idx
