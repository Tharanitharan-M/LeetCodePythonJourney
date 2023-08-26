# Problem - 347. Top K Frequent Elements:

![Medium](https://img.shields.io/badge/Medium-ffc926)

## Problem Statement:

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

Example 1:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

Example 2:

```
Input: nums = [1], k = 1
Output: [1]
```

Constraints:

- 1 <= nums.length <= 10^5
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

## Intuition

The intuition behind this solution is to find the `k` most frequent elements in the given integer array `nums`. We can solve this by using a hashmap to count the occurrences of each element in the array. Then, we can sort the elements based on their frequencies in descending order and return the top `k` elements.

## Approach

The approach involves using a hashmap to store the frequency of each element in the integer array `nums`. We iterate through the array, updating the hashmap with the count of each element. Next, we sort the elements based on their frequencies in descending order using the `sorted` function and a custom sorting key. Finally, we return the first `k` elements from the sorted list, which are the `k` most frequent elements.

## Complexity

- Time complexity: **O(n log n)**
  The time complexity of this approach is dominated by the sorting step, which takes `O(n log n)` time, where `n` is the number of elements in the array.

- Space complexity: **O(n)**
  The space complexity is determined by the space required to store the hashmap, which can store up to `n` elements in the worst case.

## Code:
[Python Code](347.%20Top%20K%20Frequent%20Elements.py)

Feel free to use this solution as a reference for solving the "347. Top K Frequent Elements" problem. This approach efficiently finds the k most frequent elements in an integer array. Happy coding! 🚀🔥