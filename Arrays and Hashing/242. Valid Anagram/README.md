# Problem 242: Valid Anagram

Difficulty: ![Easy](https://img.shields.io/badge/Easy-3fca7d)
Link: [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An anagram is a word or phrase formed by rearranging the letters of another. In this problem, we determine whether two strings are anagrams by comparing the frequency of characters in both strings.

## Intuition

The intuition behind this solution is to determine whether two input strings `s` and `t` are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of another. In this problem, we can solve it by using a hashmap to count the occurrences of characters in both strings and then comparing the counts to check if they match.

## Approach

The approach involves using a hashmap to store the character frequencies of the first string `s`. We iterate through `s`, updating the hashmap with the count of each character. Then, we iterate through the second string `t` and decrement the counts in the hashmap for each character encountered. If a character count reaches zero, we remove it from the hashmap. Finally, if the hashmap becomes empty, it indicates that the strings are anagrams.

## Complexity

- Time complexity: **O(n)**
  The time complexity of this approach is determined by two main operations. The first operation involves iterating through the characters of string `s` to build the hashmap (which takes O(n) time), and the second operation involves iterating through the characters of string `t` to update the hashmap (which also takes O(n) time in the worst case). Therefore, the overall time complexity is `O(n)`.

- Space complexity: **O(min(n, m))**
  The space complexity is determined by the space required to store the hashmap. In the worst case, when all distinct characters from both strings are stored in the hashmap, the space complexity is `O(min(n, m))`, where n is the length of string `s` and m is the length of string `t`.

## Code

[Python Code]("242. Valid Anagram.py")

Feel free to use this solution as a reference for solving the "242. Valid Anagram" problem. This approach provides an efficient solution to determine whether two strings are anagrams of each other. Happy coding! 🚀🔥
