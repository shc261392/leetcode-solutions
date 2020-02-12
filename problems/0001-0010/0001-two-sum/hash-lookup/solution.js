/**
 * Success
 * Details
 * Runtime: 56 ms, faster than 86.06% of JavaScript online submissions for Two Sum.
 * Memory Usage: 36.2 MB, less than 11.99% of JavaScript online submissions for Two Sum.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let lookup_table = new Object();
    let result = [];
    nums.forEach((num, idx) => {
        if ((target - num) in lookup_table) {
            result = [
                lookup_table[target - num],
                idx,
            ];
        }
        lookup_table[num] = idx;
    });
    return result;
};
