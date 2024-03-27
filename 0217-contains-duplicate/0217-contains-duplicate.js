/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let seen = new Set();
    for (let num of nums) {
        if (seen.has(num)) {
            return true; // 이미 보았던 숫자를 다시 봄
        }
        seen.add(num);
    }
    return false; // 중복된 숫자 없음
};
