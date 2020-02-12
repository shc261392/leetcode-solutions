/**
 * Success
 * Details
 * Runtime: 172 ms, faster than 12.94% of JavaScript online submissions for Add Two Numbers.
 * Memory Usage: 38.9 MB, less than 18.05% of JavaScript online submissions for Add Two Numbers.
 * Seems there's a lot of room for improvement
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let v1, v2, overflow = 0;
    let first_node = null, previous_node = null;

    while (l1 !== null || l2 !== null || overflow !== 0) {
        v1 = (l1 === null) ? 0 : l1.val;
        v2 = (l2 === null) ? 0 : l2.val;
        temp_sum = v1 + v2 + overflow;
        v3 = (temp_sum) % 10;
        overflow = Math.floor((temp_sum) / 10);
        l3 = new ListNode(v3);
        if (first_node === null) {
            first_node = l3;
        } else {
            previous_node.next = l3;
        }
        previous_node = l3;

        if (l1 !== null) l1 = l1.next;
        if (l2 !== null) l2 = l2.next;
    }
    return first_node
};
