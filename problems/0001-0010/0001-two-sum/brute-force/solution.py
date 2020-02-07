class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        for index_a, value_a in enumerate(nums):
            for index_b, value_b in enumerate(nums):
                if index_a == index_b:
                    continue
                if value_a + value_b == target:
                    return [index_a, index_b]
