/**
 * Two Sum in unsorted Array
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const nums = [3, 2, 4];
const target = 6;
var twoSum = function (nums, target) {
  let map = {};
  for (let i = 0; i < nums.length; i++) {
    if (target - nums[i] in map) {
      return [map[target - nums[i]], i];
    } else {
      map[nums[i]] = i;
    }
  }
};

console.log(twoSum());







/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function (functions) {
    return new Promise((resolve, reject) => {
        const completed = 0
        const results = []
        functions.forEach((fn, index) => {
            fn()
                .then((result) => {
                    results[index] = result
                    completed += 1
                    if (completed === functions.length) {
                        resolve(results)
                    }
                })
                .catch((error) => {
                    reject(error)
                })
        })
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */