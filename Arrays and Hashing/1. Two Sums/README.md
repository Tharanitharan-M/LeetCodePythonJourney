# 1. Two Sum 🎯

- Difficulty: ![Easy](https://img.shields.io/badge/Easy-3fca7d)
- Link: [Two Sum](https://leetcode.com/problems/two-sum/)

## Problem Statement 📜

Given an array of integers `nums` and an integer `target`, your task is to find two distinct numbers in the array that sum up to the `target`. You need to return the indices of these two numbers.

Assume that each input will have exactly one solution, and you cannot use the same element twice to form the sum.

You are free to return the answer in any order.

## Intuition 🤔

The essence of this problem lies in identifying pairs of numbers that add up to a specific target value. To approach this efficiently, a hash map (dictionary in Python) can be employed. This involves iterating through the array, and for each element, checking whether the difference between the target value and the current element exists in the hash map. If such a difference is present, a valid pair has been located.

## Approach 🛤️

1. Create an empty hash map named `sumsDict` to store values and their corresponding indices.
2. Iterate through the array using `enumerate`, obtaining the index `i` and value `num`.
   - Calculate the difference `diff` between `target` and `num`.
   - Check if `diff` is already present in the hash map.
     - If `diff` is found, return the indices `[sumsDict[diff], i]`.
     - If not, add the current `num` to the hash map with index `i`.
3. If no valid solution is found during the iteration, return an empty list.

## Complexity ⏳

- Time Complexity: **O(n)**
  - The use of a hash map allows constant time access to stored values.
  - The iteration through the array occurs only once.

- Space Complexity: **O(n)**
  - The hash map potentially stores up to `n` elements, where `n` is the size of the input array.

## Code 🚀

[Python Code](1.%20Two%20Sum.py)

Feel free to explore various strategies and approaches. If you encounter any uncertainties or potential enhancements, don't hesitate to reach out for guidance or discussion. Best of luck in your coding endeavors! 🌟💻
