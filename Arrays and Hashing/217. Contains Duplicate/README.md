# Problem 217: Contains Duplicate

- Difficulty: ![Easy](https://img.shields.io/badge/Easy-3fca7d)
- Link: [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Intuition

The intuition behind this solution is to determine whether the input integer array `nums` contains any duplicate elements. We can solve this by using a hashmap to keep track of the elements we have encountered. If we encounter an element that is already present in the hashmap, it means there is a duplicate and we return `True`. Otherwise, if we iterate through the entire array without finding any duplicates, we return `False`.

## Approach

The approach involves using a hashmap to store the elements of the integer array `nums`. We iterate through the array, and for each element, we check if it is already present in the hashmap. If it is, we return `True`, indicating the presence of a duplicate. Otherwise, we add the element to the hashmap. If we complete the iteration without finding any duplicates, we return `False`.

## Complexity

- Time complexity: **O(n)**
  The time complexity of this approach is determined by the number of elements in the array. In the worst case, we iterate through the entire array once, resulting in a time complexity of `O(n)`.

- Space complexity: **O(n)**
  The space complexity is determined by the space required to store the hashmap. In the worst case, when all elements in the array are distinct, the space complexity is `O(n)`.

## Code
[Python Code](217.%20Contains%20Duplicate.py)

Feel free to use this solution as a reference for solving the "242. Valid Anagram" problem. This approach provides an efficient solution to determine whether two strings are anagrams of each other. Happy coding! 🚀🔥
