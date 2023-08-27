# 128. Longest Consecutive Sequence 🎯

- Difficulty: ![Medium](https://img.shields.io/badge/Medium-ffc926)
- Link: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem Statement 📜

Welcome to the world of sequence exploration! Your noble task is to find the length of the longest consecutive elements sequence from an array of integers.

A consecutive sequence is a sequence of consecutive numbers that are present in the array. The sequence does not necessarily need to be in sorted order. Your quest is to uncover this longest consecutive sequence and reveal its length.

Embark on this journey and unravel the secrets of consecutive sequences! 🌟🔢

## Intuition 🤔

The essence of this problem lies in identifying consecutive sequences of numbers within the given array. One approach involves leveraging hash sets to efficiently check for the existence of consecutive elements. By iterating through the array, you can track the length of sequences starting from each unique number.

## Approach 🛤️

1. Transform the `nums` array into a hash set for efficient element lookup.
2. Initialize a variable `result` to store the length of the longest sequence.
3. For each element `num` in the hash set:
   - Check if `num - 1` is not present in the hash set (indicating the start of a new sequence).
   - If not, initialize a variable `length` as 1 and enter a loop.
   - While `num + 1` is present in the hash set, increment `length` and `num`.
   - Update `result` with the maximum of `result` and `length`.
4. Return the final `result` as the length of the longest consecutive sequence.

## Complexity ⏳

- Time Complexity: **O(n)**

  - Iterating through the array to populate the hash set takes O(n) time.
  - The subsequent loop to find consecutive sequences also takes O(n) time in the worst case.

- Space Complexity: **O(n)**
  - The hash set stores unique elements from the input array.

## Code 🚀

[Python Code](128.%20Longest%20Consecutive%20Sequence.py)

Feel free to explore alternative strategies and optimizations. If you encounter questions or seek to discuss potential enhancements, please don't hesitate to reach out. Best of luck on your journey to uncover the longest consecutive sequence! 🌟💻
