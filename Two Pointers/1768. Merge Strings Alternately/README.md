# 1768. Merge Strings Alternately 🎯

- Difficulty: ![Easy](https://img.shields.io/badge/Easy-3fca7d)
- Link: [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)

## Problem Statement 📜

Welcome to the realm of string merging! Your mission is to merge two strings alternately, taking one character at a time from each string. If one string becomes empty before the other, continue merging characters from the remaining string.

Your quest is to unveil the result of this mesmerizing merging dance! 🌟🔤

## Intuition 🤔

Merge strings alternately by iteratively selecting characters from both strings, one by one. Use separate pointers or indices to keep track of the current position in each string. Combine the selected characters into a new string to create the merged result.

## Approach 🛤️

1. Initialize an empty string named `result` to store the merged result.
2. Use a `while` loop to iterate while both `word1` and `word2` are non-empty:
   - If `word1` is non-empty, append its first character to `result` and remove it.
   - If `word2` is non-empty, append its first character to `result` and remove it.
3. After the loop, if any characters remain in `word1`, append them to `result`.
4. Similarly, if any characters remain in `word2`, append them to `result`.
5. Return the final `result` as the merged string.

## Complexity ⏳

- Time Complexity: **O(n + m)**

  - The loop iterates through both `word1` and `word2`, each of length n and m respectively.
  - The append and removal operations take constant time.

- Space Complexity: **O(n + m)**
  - The `result` string stores the merged characters.

## Code 🚀

[Python Code](1768.%20Merge%20Strings%20Alternately.py)

Feel free to explore alternative strategies and enhancements. If you encounter questions or seek to discuss potential improvements, please don't hesitate to reach out. May your journey of string merging be filled with success! 🌟💻
