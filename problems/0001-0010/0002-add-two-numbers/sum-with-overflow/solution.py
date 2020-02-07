"""
Success
Details
Runtime: 68 ms, faster than 70.02% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.

Seems too ugly. I believe there are cleaner ways to do this...
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def node_sum(v1, v2, overflow):
            temp_sum = v1 + v2 + overflow
            return temp_sum % 10, int(temp_sum / 10)

        overflow = 0
        first_node = None
        l3_last_node = None
        while True:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            l3 = ListNode(0)
            l3.val, overflow = node_sum(v1, v2, overflow)
            if l3.val == 0 and overflow == 0 and (not l1 and not l2):
                break
            if not first_node:
                first_node = l3
            if l3_last_node:
                l3_last_node.next = l3
            l3_last_node = l3

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return first_node

