# 49. Group Anagrams

- Difficulty: ![Medium](https://img.shields.io/badge/Medium-ffc926)
- Link: [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

## Problem Statement

Given an array of strings `strs`, your task is to group the anagrams together. Two strings are considered anagrams if they have the same set of characters, regardless of their order.

## Intuition

The essence of this problem lies in identifying strings that share the same characters, albeit in different orders. To solve this, one can employ a strategy of mapping each string to a representative structure, like a sorted version of the characters. This allows grouping anagrams under a common key.

## Approach

1. Create a hash map to hold anagrams grouped by their character frequency counters.
2. Iterate through each string in the input `strs` array.
   - Count the frequency of each character in the current string using a counter array.
   - Convert the counter array to a tuple and use it as a key to the hash map.
   - Append the current string to the list of anagrams under the computed key.
3. Return the values (lists of anagrams) from the hash map.

## Complexity

- Time Complexity: **O(n \* k)**

  - Iterating through the array requires O(n) time.
  - Counting the frequency of characters in each string takes O(k) time.

- Space Complexity: **O(n \* k)**
  - The hash map can potentially store all strings.

## Code

[Python Code](49.%20Group%20Anagrams.py)

Feel free to explore alternative approaches and optimizations. Should you encounter questions or seek to discuss potential enhancements, please don't hesitate to reach out. Best of luck with your coding endeavors!
