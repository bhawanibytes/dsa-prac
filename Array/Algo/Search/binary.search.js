

/**
 * binary Search assume given array is sorted
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const nums = [3, 2, 4];
const target = 6;
var twoSum = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;
  while (left < right) {
    const sum = nums[left] + nums[right];
    if (sum === target) {
      return [left, right];
    } else if (sum > target) {
      right--;
    } else {
      left++;
    }
  }
};
console.log(twoSum())