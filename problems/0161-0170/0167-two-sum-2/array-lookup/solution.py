"""
Success
Details
Runtime: 2392 ms, faster than 5.05% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.

So slow! It's O(n^2)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, number in enumerate(numbers):
            if (target - number) in numbers:
                if numbers.index(target - number) == idx:
                    numbers[idx] = numbers[idx] + 1
                idy = numbers.index(target - number)
                return [
                    idx + 1,
                    idy + 1,
                ]
